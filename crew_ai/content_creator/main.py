#!/usr/bin/env python
import sys
import os


# SET OPENAI_API_KEY ENVIRONMENT VARIALBE
# SET OPENAI_MODEL_NAME ENVIRONMENT VARIABLE
# SET SERPER KEY ENVIRONMENT VARIABLE

import erppeek


from crew import (
    CrewaiEnterpriseContentMarketingCrew,
)




def run():
    """
    Run the crew.
    """
    topic = input('Enter your topic : ')
    company = input('Enter the company : ')
    inputs = {"topic": topic, "company": company}

    result = CrewaiEnterpriseContentMarketingCrew().crew().kickoff(inputs=inputs)

    return result

res = run()
result = res.pydantic.dict()
print(result)

# CREATE A BLOG POST
# ODOO_URL = "http://127.0.0.1:8069/"
# ODOO_DB = "chatbot"
# ODOO_USER = "admin"
# ODOO_PASSWORD = "Testing1"

# # Connect to Odoo
# client = erppeek.Client(server=ODOO_URL, db=ODOO_DB, user=ODOO_USER, password=ODOO_PASSWORD)

# # Model name for blog posts
# model = "blog.post"


# blog_post_id = client.create(model, result)

