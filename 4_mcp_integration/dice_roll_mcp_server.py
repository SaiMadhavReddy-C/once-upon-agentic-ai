from mcp.server import FastMCP
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

mcp = FastMCP("D&D Dice Roll Service", port=8002)


@mcp.tool()
def roll_dice(faces: int = 6, count: int = 1) -> dict:
    """
    Roll multiple dice with a specified number of faces.

    Args:
        faces: Number of faces on the dice.
        count: Number of dice to roll.

    Returns:
        Dictionary containing the dice results and number of faces.
    """
    if faces < 1:
        error_msg = "Dice must have at least 1 face"
        logging.warning(f"🎲 Invalid dice roll request: {error_msg}")
        return {"error": error_msg}

    if count < 1:
        error_msg = "Must roll at least 1 dice"
        logging.warning(f"🎲 Invalid dice roll request: {error_msg}")
        return {"error": error_msg}

    results = [random.randint(1, faces) for _ in range(count)]

    logging.info(f"🎲 DICE ROLL: {count}d{faces} = {results}")

    return {
        "results": results,
        "faces": faces
    }


if __name__ == "__main__":
    print("Starting D&D Dice Roll MCP Server...")
    mcp.run(transport="streamable-http")
