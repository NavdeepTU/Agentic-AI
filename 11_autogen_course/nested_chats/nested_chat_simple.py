import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "temperature": 0.4,
    "api_key": os.environ["OPENAI_API_KEY"]
}

# Define the writer agent
writer = AssistantAgent(
    name="Writer",
    llm_config=llm_config,
    system_message="""
    You are a professional writer, known for your insightful and engaging product reviews.
    You transform technical details into compelling narratives.
    You should improve the quality of the content based on the feedback from the user.
    """,
)

# Define the user proxy agent
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "my_code",
        "use_docker": False,
    },
)

# Define the critic agent
critic = AssistantAgent(
    name="Critic",
    llm_config=llm_config,
    system_message="""
    You are a critic, known for your thoroughness and commitment to standards.
    Your task is to scrutinize content for any harmful elements or regulatory violations, ensuring
    all materials align with required guidelines.
    """,
)

# function to generate reflection message
def reflection_message(recepient, messages, sender, config):
    print("Reflecting...")
    return f"Reflect and provide critique on the following review. \n\n {recepient.chat_messages_for_summary(sender)[-1]['content']}"

# register nested chats with the user proxy agent
user_proxy.register_nested_chats(
    [
        {
            "recipient": critic,
            "message": reflection_message,
            "summary_method": "last_msg",
            "max_turns": 1
        }
    ],
    trigger=writer
)

# define the task
task = """Write a detailed and engaging product review for the new Meta VR headset."""

# start the nested chat
res = user_proxy.initiate_chat(
    recipient=writer, message=task, max_turns=2, summary_method="last_msg"
)