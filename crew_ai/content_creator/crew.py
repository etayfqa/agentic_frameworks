from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,CSVSearchTool

from typing import List
from pydantic import BaseModel, Field

class BlogPost(BaseModel):
    id: int = Field(default=1, description="Unique identifier for the blog post")  # Default ID
    name: str = Field(..., description="Name of the blog")
    subtitle: str = Field(..., description="Subtitle of the blog")
    content: str = Field(default="<h1>Default Blog Title</h1><p>Default blog content.</p>", description="Content of the blog")
    website_meta_title: str = Field(..., description="Meta title of the blog")
    website_meta_description: str = Field(..., description="Meta description of the blog")
    website_meta_keywords: str = Field(..., description="Meta keywords of the blog")
    #key_words: List[str] = Field(..., description="List of resources required to complete the task")

csv_tool = CSVSearchTool(csv='content/topics.csv')
scrap_tool = ScrapeWebsiteTool(website_url='https://www.oksouq.com')
search_tool = SerperDevTool()
@CrewBase
class CrewaiEnterpriseContentMarketingCrew:
    """CrewaiEnterpriseContentMarketing crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config["planner"],
            tools=[search_tool],  # Add tools suitable for planning
            verbose=True,
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            tools=[search_tool],  # Add tools suitable for writing
            verbose=True,
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            tools=[],  # Add tools suitable for editing
            verbose=True,
        )
   

    @task
    def plan(self) -> Task:
        return Task(
            config=self.tasks_config["plan"],
            output_file="plan_report.json",
            # Uncomment and define the Pydantic model if required
            # output_pydantic=PlanOutputModel
        )

    @task
    def write(self) -> Task:
        return Task(
            config=self.tasks_config["write"],
            output_file="blog_post.md",
            # Uncomment and define the Pydantic model if required
            # output_pydantic=BlogPost
        )

    @task
    def edit(self) -> Task:
        return Task(
            config=self.tasks_config["edit"],
            #output_file="final_blog_post.md",
            # Uncomment and define the Pydantic model if required
            output_pydantic=BlogPost
        )

    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["research_task"],
    #          output_file="report.json",
    #          #output_pydantic=BlogPost
    #     )
    # @agent
    # def writer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["writer"],
    #         tools=[search_tool],
    #         verbose=True,
    #     )

  

    # @task
    # def blog_post_writing_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["blog_post_writing_task"],
    #          output_file="blog.json",
    #          output_pydantic=BlogPost
    #     )

  

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiEnterpriseContentMarketing crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
          
        )
