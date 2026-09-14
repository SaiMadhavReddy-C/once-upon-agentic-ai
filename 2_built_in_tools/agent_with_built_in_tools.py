from strands import Agent
from strands_tools import current_time

# Create an agent with the current_time built-in tool
agent = Agent(
    system_prompt=(
        "You are a helpful assistant. "
        "When the user asks about the current time or date, "
        "use the current_time tool to get the accurate answer."
    ),
    tools=[current_time],
)

# Ask the agent a time-related question
agent("What time is it?")
