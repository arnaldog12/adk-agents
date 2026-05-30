"""Level 2: Session + Memory + callbacks."""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool


async def auto_save_session_to_memory_callback(callback_context):
    """Auto save session to memory."""
    await callback_context.add_session_to_memory()


root_agent = Agent(
    model="gemini-2.5-flash",
    name="level_2",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[PreloadMemoryTool()],
    after_agent_callback=[auto_save_session_to_memory_callback],
)
