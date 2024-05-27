import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model_name = os.getenv('OPENAI_MODEL_NAME')
huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
exa_api_key = os.getenv('EXA_API_KEY')
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
langchain_tracing_v2 = os.getenv('LANGCHAIN_TRACING_V2')

from crewai import Crew
from langchain_community.llms import HuggingFaceHub
from agents import MeetingPrepAgents
from tasks import MeetingPrepTasks


llm = HuggingFaceHub(repo_id="google/gemma-2b-it", model_kwargs={"max_new_tokens": 250})

# researcher = MeetingPrepAgents().researcher()
writer = MeetingPrepAgents().writer()

# listdownjobs_task = MeetingPrepTasks(agent=researcher).Listdownjobs()
developblog_task = MeetingPrepTasks(agent=writer).develop_blog()
crew = Crew(
    agents=[writer],
    tasks=[developblog_task],
    verbose=2
)
results = crew.kickoff()
print(results)