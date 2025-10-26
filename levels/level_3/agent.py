from google.adk.agents.llm_agent import Agent

from .prompt import agent_instruction
from .tools.tools import get_current_date, search_tool, toolbox_tools

root_agent = Agent(
    model="gemini-2.5-flash",
    name="level_3",
    instruction=agent_instruction,
    tools=[get_current_date, search_tool, *toolbox_tools],
)
