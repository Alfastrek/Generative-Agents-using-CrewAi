from crewai import Agent
from tools import ExaSearchToolset

class MeetingPrepAgents():
    def researcher(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Top tech jobs in 2024',
            # tools=[ExaSearchToolset()],
            backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
        )
    def writer(self):
        return Agent(
            role='Tech content Strategist',
            goal='Craft compelling content based on tech job advancements',
            # tools=[ExaSearchToolset()],
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. You transform
            complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=False,
        ) 

