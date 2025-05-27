from autogen import ConversableAgent
import os
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY"),
    "temperature": 0.9
}

boss = ConversableAgent(
    name="Abhinav",
    system_message="You are manager in the company google. " \
                    "You are very nice person loved by everyone " \
                    "around you. When you want the conversation to end," \
                    "you politely say good bye.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    # max_consecutive_auto_reply=1
)

employee = ConversableAgent(
    name="Ajay",
    system_message="You are an sincere and disciplined employee of google. Your manager is Abhinav.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "goodbye" in msg["content"].lower()
)

result = employee.initiate_chat(boss, message="Abhinav, I need a holiday for 2 days.", max_turns=4)