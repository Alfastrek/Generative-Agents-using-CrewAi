import os
from dotenv import load_dotenv

load_dotenv()

# Assuming you have set up these environment variables correctly
huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
gemini_api_token=os.getend('GEMINI_API_TOKEN')pip install langchain-core>=0.1.42,<0.2.0pip install langchain-core>=0.1.42,<0.2.0pip uninstall langchain langchain-core langchain-community langchain-openai langchain-text-splitters -y

import os
from dotenv import load_dotenv
from crewai import Crew
from langchain_community.llms import HuggingFaceHub
from agents import MeetingPrepAgents
from tasks import MeetingPrepTasks

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face Hub API token from environment variables
huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Check if the API token is loaded
if huggingfacehub_api_token is None:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set")

# Initialize the HuggingFaceHub with the API token
llm = HuggingFaceHub(repo_id="google/gemma-2b-it", model_kwargs={"max_new_tokens": 250})

# Initialize agents and tasks
writer = MeetingPrepAgents().writer()
developblog_task = MeetingPrepTasks(agent=writer).develop_blog()

# Create a Crew instance
crew = Crew(
    agents=[writer],
    tasks=[developblog_task],
    verbose=2
)

# Kickoff the crew and print results
results = crew.kickoff()
print(results)
