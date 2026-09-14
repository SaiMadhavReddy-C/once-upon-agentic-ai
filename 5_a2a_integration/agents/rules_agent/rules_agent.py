from strands import Agent, tool
from strands.multiagent.a2a import A2AServer


@tool
def query_dnd_rules(query: str) -> str:
    """
    Answer common D&D rules questions.
    """
    q = query.lower()

    if "attack roll" in q or "d20" in q:
        return "An attack roll normally uses a d20 plus the appropriate modifier."

    if "4d6" in q or "ability score" in q:
        return "The traditional ability-score method is 4d6, dropping the lowest die."

    if "initiative" in q:
        return "Initiative normally uses a d20 plus the Dexterity modifier."

    if "armor class" in q or " ac " in f" {q} ":
        return "Armor Class (AC) determines how difficult a target is to hit."

    if "saving throw" in q:
        return "A saving throw normally uses a d20 plus the relevant ability modifier."

    return "That rule is not covered by this simplified rules service."


def create_agent(context_id: str) -> Agent:
    return Agent(
        name="Rules Agent",
        description="A D&D rules specialist.",
        system_prompt=(
            "You are a D&D rules expert. "
            "Use the query_dnd_rules tool to answer rules questions "
            "and keep the answer concise."
        ),
        tools=[query_dnd_rules],
    )


a2a_server = A2AServer(
    agent_factory=create_agent,
    port=8000,
)


if __name__ == "__main__":
    print("📚 Rules Agent running on http://127.0.0.1:8000")
    a2a_server.serve()
