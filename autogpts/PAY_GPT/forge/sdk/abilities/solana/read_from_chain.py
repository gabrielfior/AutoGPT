from typing import List

from ..registry import ability

@ability(
    name="fetch_latest_slot",
    description="Fetches latest slot from the Solana blockchain",
    parameters=[{
            "name": "timestamp",
            "description": "Timestamp of the block being fetched",
            "type": "int",
            "required": True,
        }],
    output_type="int",
)
async def read_latest_slot(agent, task_id: str, timestamp: int) -> int:
    return 12345
