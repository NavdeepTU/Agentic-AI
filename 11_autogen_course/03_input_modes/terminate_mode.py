import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

agent_with_animal = ConversableAgent(
    "agent_with_animal",
    system_message="You are thinking of an animal." \
    "You have the animal 'elephant' in your mind, and I will try to guess it. " \
    "If I guess incorrectly, give me a hint.",
    llm_config=llm_config,
    max_consecutive_auto_reply=1, # maximum number of consecutive auto-replies before asking for human input
    is_termination_msg=lambda msg: "elephant" in msg["content"], # terminate if the animal is guessed by the other agent
    human_input_mode="TERMINATE", # ask for human input until the game is terminated
)

agent_guess_animal = ConversableAgent(
    "agent_guess_animal",
    system_message="I have an animal in my mind, and you will try to guess it. " \
    "If I give out a hint, use it to narrow down your guesses.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

agent_with_animal.initiate_chat(
    agent_guess_animal,
    message="I am thinking of an animal. Guess which one!"
)