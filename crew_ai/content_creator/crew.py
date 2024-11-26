from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from crewai_enterprise_content_marketing_ideas.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,CSVSearchTool

from typing import List
from pydantic import BaseModel, Field

class BlogPost(BaseModel):
    title: str = Field(..., description="Name of the task")
    brief_explanation: str = Field(..., description="Estimated time to complete the task in hours")
    key_words: List[str] = Field(..., description="List of resources required to complete the task")
# Initialize the tool to search within any DOCX file's content

# OR

# Initialize the tool with a specific DOCX file, 
# so the agent can only search the content of the specified DOCX file
#txt_tool = TXTSearchTool(txt='/Users/semirworku/Documents/GitHub/agentic_frameworks/crew_ai/content_creator_2/content/topics.txt')
csv_tool = CSVSearchTool(csv='content/topics.csv')
scrap_tool = ScrapeWebsiteTool(website_url='https://www.oksouq.com')
search_tool = SerperDevTool()
@CrewBase
class CrewaiEnterpriseContentMarketingCrew:
    """CrewaiEnterpriseContentMarketing crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[scrap_tool,csv_tool ,search_tool],
            verbose=True,
        )

  

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
             output_file="report.json",
             output_pydantic=BlogPost
        )

  

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiEnterpriseContentMarketing crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
