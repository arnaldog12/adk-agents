from google.adk.agents.llm_agent import Agent

from .tools import run_python_code

developer = Agent(
    name="developer",
    model="gemini-2.5-flash",
    description="A developer who is responsible for implementing the {product_features} using Python.",
    instruction="""
    Implement the product features using Python. 
    You only write functions and classes that are related to the product features.
    You can use the run_python_code tool to check syntax errors.
    You never write infinite loops.
    Do not write code to test the code you write. There is a separate QA engineer agent for that.
    You always write code that is safe and secure.
    Once you have written the code, run it using the run_python_code tool.
    """,
    tools=[run_python_code],
    output_key="generated_code",
)

qa_engineer = Agent(
    name="qa_engineer",
    model="gemini-2.5-flash",
    description="A QA engineer who is responsible for testing the {generated_code} using Python.",
    instruction="""
    Test Python code and report any errors or issues.
    Always show the test code you wrote to the user.
    """,
    tools=[run_python_code],
    output_key="test_results",
)

product_manager = Agent(
    name="product_manager",
    model="gemini-2.5-flash",
    description="A product manager who is responsible for define a list of product features.",
    instruction=""""
    You are a product manager who is responsible for define a list of product features.
    You start by defining the product features.
    Once you have it, confirm with the user if the product features are correct.
    Once the user confirms the product features, delegate the task to the developer agent.
    When the developer agent has finished implementing the product features, delegate the task to the qa_engineer agent.
    When the qa_engineer agent has finished testing the product features, return the final code to the user.
    """,
    sub_agents=[developer, qa_engineer],
    output_key="product_features",
)

root_agent = product_manager
