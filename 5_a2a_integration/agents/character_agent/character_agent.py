import uuid
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict

from strands import Agent, tool
from strands.multiagent.a2a import A2AServer
from tinydb import TinyDB, Query


@dataclass
class Stats:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@dataclass
class InventoryItem:
    item_name: str
    quantity: int


@dataclass
class Character:
    character_id: str
    name: str
    character_class: str
    race: str
    gender: str
    level: int
    experience: int
    stats: Stats
    inventory: List[InventoryItem]
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()


characters_db = TinyDB("characters.json")
Character_Query = Query()


@tool
def create_character(
    name: str,
    character_class: str,
    race: str,
    gender: str,
    stats_dict: Dict[str, int],
) -> str:
    """Create and store a D&D character."""

    character = Character(
        character_id=str(uuid.uuid4()),
        name=name,
        character_class=character_class,
        race=race,
        gender=gender,
        level=1,
        experience=0,
        stats=Stats(
            strength=stats_dict.get("strength", 10),
            dexterity=stats_dict.get("dexterity", 10),
            constitution=stats_dict.get("constitution", 10),
            intelligence=stats_dict.get("intelligence", 10),
            wisdom=stats_dict.get("wisdom", 10),
            charisma=stats_dict.get("charisma", 10),
        ),
        inventory=[
            InventoryItem("Starting Equipment Pack", 1),
            InventoryItem("Gold Pieces", 100),
        ],
    )

    characters_db.insert(asdict(character))
    return f"Character created successfully: {character}"


@tool
def find_character_by_name(name: str) -> str:
    """Find a character by name."""

    result = characters_db.search(Character_Query.name == name)

    if not result:
        return f"Character '{name}' not found."

    return str(result[0])


@tool
def list_all_characters() -> str:
    """List all characters."""

    characters = characters_db.all()

    if not characters:
        return "No characters found."

    return str(characters)


def create_agent(context_id: str) -> Agent:
    return Agent(
        name="Character Creator Agent",
        description="Creates and manages D&D characters.",
        system_prompt=(
            "You are a D&D character management specialist. "
            "Use your tools to create, find, and list characters."
        ),
        tools=[
            create_character,
            find_character_by_name,
            list_all_characters,
        ],
    )


a2a_server = A2AServer(
    agent_factory=create_agent,
    port=8001,
)


if __name__ == "__main__":
    print("🎭 Character Agent running on http://127.0.0.1:8001")
    a2a_server.serve()
