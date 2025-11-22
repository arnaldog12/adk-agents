from google.adk.agents.llm_agent import Agent

from level_1.prompt import agent_instruction
from level_1.tools.tools import get_current_date, search_tool, toolbox_tools

root_agent = Agent(
    model="gemini-2.5-flash",
    name="level_1",
    instruction=agent_instruction,
    tools=[get_current_date, search_tool, *toolbox_tools],
)
