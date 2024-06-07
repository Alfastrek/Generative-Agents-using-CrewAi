from crewai import Task

class MeetingPrepTasks:
    def __init__(self, agent):
        self.agent = agent

    def Listdownjobs(self):
        return Task(
            description="""List down Top Tech job roles.""",
            expected_output="Full analysis report in short bullet points",
            agent=self.agent
        )
    
    def developblog(self):
        return Task(
            description="""Using the insights provided, develop an engaging blog that posts the highlights of the most significant and
            high-paying tech jobs in 2024.""",
            expected_output="Full blog post of at least 4 paragraphs",
            agent=self.agent
        )
