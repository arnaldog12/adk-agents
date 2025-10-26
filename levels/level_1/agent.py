from google.adk.agents.llm_agent import Agent


def count_words(text: str) -> int:
    """Counts the number of words in a given text."""
    return {
        "status": "success",
        "result": len(text.split()),
    }


root_agent = Agent(
    name="level_1",
    model="gemini-2.5-flash",
    description="An agent to generates texts with a given number of words.",
    instruction="Generate a text with a given number of words.",
    tools=[count_words],
)
