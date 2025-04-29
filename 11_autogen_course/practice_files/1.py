import os
from autogen import AssistantAgent, ConversableAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=llm_config,
    code_execution_config={
        "work_dir": "code_execution_files",
        "use_docker": False
    },
    human_input_mode="ALWAYS"
)

user_proxy.initiate_chat(
    assistant,
    message="Tell me who one todays match between Rockets and Warriors?"
)