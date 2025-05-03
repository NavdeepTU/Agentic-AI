import os
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent
from typing import Annotated
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "temperature": 0.9,
    "api_key": os.environ["OPENAI_API_KEY"]
}

# the initial agent always returns a given text
initial_agent = ConversableAgent(
    name="Initial_Agent",
    system_message="You return me the text I give you.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# the uppercase agent converts the text into uppercase.
uppercase_agent = ConversableAgent(
    name="Uppercase_agent",
    system_message="You convert the text i give you to uppercase.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# the word count agent counts the number of words in the text.
word_count_agent = ConversableAgent(
    name="WordCount_Agent",
    system_message="You count the number of words in the text I give you.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# the reverse text agent reverses the text
reverse_text_agent = ConversableAgent(
    name="ReverseText_Agent",
    system_message="You reverse the text I give you.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# the summarize agent summarizes the text
summarize_agent = ConversableAgent(
    name="Summarize_Agent",
    system_message="You summarize the text I give you.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)