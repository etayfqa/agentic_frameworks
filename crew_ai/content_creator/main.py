#!/usr/bin/env python
import sys
import os


from crew import (
    CrewaiEnterpriseContentMarketingCrew,
)




def run():
    """
    Run the crew.
    """
    inputs = {"topic": "buy used smartwatch", "company": "OkSouQ Qatar"}

    result = CrewaiEnterpriseContentMarketingCrew().crew().kickoff(inputs=inputs)

    return result

res = run()
print(res.pydantic.dict()['title'])


