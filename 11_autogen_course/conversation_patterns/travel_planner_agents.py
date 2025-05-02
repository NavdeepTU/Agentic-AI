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

travel_agent = ConversableAgent(
    name="Travel_Agent",
    system_message="You are a traveler planning a vacation.",
    llm_config=llm_config
)

guide_agent = ConversableAgent(
    name="Guide_Agent",
    system_message="You are a travel guide with extensive knowledge about popular destinations.",
    llm_config=llm_config
)

chat_result = travel_agent.initiate_chat(
    guide_agent,
    message="What are the must-see attractions in Tokyo?",
    summary_method="reflection_with_llm", # use the llm to summarize the chat history
    max_turns=2
)

print(chat_result)

# ChatResult(
# chat_id=None, 
# chat_history=[{'content': 'What are the must-see attractions in Tokyo?', 'role': 'assistant', 'name': 'Travel_Agent'}, 
#               {'content': "Tokyo is a vibrant metropolis with a lot to offer visitors. Some must-see attractions in Tokyo include:\n\n
#                            1. Tokyo Skytree - An iconic landmark and the tallest structure in Japan, offering panoramic views of the city from its observation decks.\n
#                            2. Senso-ji Temple - Tokyo's oldest and most famous temple located in Asakusa, known for its impressive gate, Nakamise shopping street, and traditional atmosphere.\n
#                            3. Meiji Shrine - A serene Shinto shrine located in the heart of Tokyo's bustling Harajuku district, surrounded by a lush forest.\n
#                            4. Tsukiji Fish Market - A bustling seafood market where you can experience the vibrant atmosphere and try fresh sushi and other seafood dishes.\n
#                            5. Shibuya Crossing - One of the busiest pedestrian crossings in the world, located in the trendy Shibuya district, offering a unique and energetic experience.\n
#                            6. Shinjuku Gyoen National Garden - A beautiful park in the heart of Tokyo, perfect for relaxing and enjoying nature in the midst of the city.\n
#                            7. Odaiba - A futuristic entertainment district on a man-made island in Tokyo Bay, known for its shopping malls, theme parks, and stunning waterfront views.\n
#                            8. Akihabara - Tokyo's electric town, famous for its electronics shops, anime and manga stores, and vibrant geek culture.\n
#                            9. Roppongi Hills - A modern complex in Roppongi offering shopping, dining, art exhibits, and stunning views of the city from its observation deck.\n
#                           10. Tokyo Disneyland and Tokyo DisneySea - Two popular theme parks that offer a magical experience for visitors of all ages.\n\n
#                           These are just a few of the many amazing attractions Tokyo has to offer. Each one provides a unique and unforgettable experience that showcases the rich culture and diverse offerings of this incredible city.", 'role': 'user', 'name': 'Guide_Agent'}, 
#               {'content': 'I hope this information helps you plan your trip to Tokyo! Let me know if you need any more assistance or recommendations.', 'role': 'assistant', 'name': 'Travel_Agent'}, 
#               {'content': "Thank you for the detailed information! I will definitely refer back to your recommendations while planning my trip to Tokyo. If I have any more questions or need further assistance, I'll be sure to reach out.", 'role': 'user', 'name': 'Guide_Agent'}], 
# summary='The travel agent provided must-see attractions in Tokyo, including the Tokyo Skytree, Senso-ji Temple, Meiji Shrine, Tsukiji Fish Market, Shibuya Crossing, and more. The agent offered assistance for trip planning and additional recommendations if needed.', 
# cost={'usage_including_cached_inference': {'total_cost': 0.0014175, 'gpt-3.5-turbo-0125': {'cost': 0.0014175, 'prompt_tokens': 1377, 'completion_tokens': 486, 'total_tokens': 1863}}, 'usage_excluding_cached_inference': {'total_cost': 0.0014175, 'gpt-3.5-turbo-0125': {'cost': 0.0014175, 'prompt_tokens': 1377, 'completion_tokens': 486, 'total_tokens': 1863}}}, 
# human_input=[])

print("\n ***Chat Summary***: \n")
print(chat_result.summary) # summary is a property of the chat result
# The travel agent provided must-see attractions in Tokyo, 
# including the Tokyo Skytree, Senso-ji Temple, Meiji Shrine, 
# Tsukiji Fish Market, Shibuya Crossing, and more. 
# The agent offered assistance for trip planning and additional 
# recommendations if needed.', 
print(ConversableAgent.DEFAULT_SUMMARY_PROMPT) # summary prompt used to generate summary from chat history
# Summarize the takeaway from the conversation. Do not add any introductory phrases.


