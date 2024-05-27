from crewai import Agent
from tools import ExaSearchToolset

class MeetingPrepAgents():
    
    def writer(self):
        return Agent(
            role='Content writer',
            goal='Craft compelling content based on given data',
            # tools=[ExaSearchToolset()],
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. You transform
            complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=False,
        ) 

