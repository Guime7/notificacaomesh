from typing import TypedDict, List

class PartitionInputList(TypedDict):
    Values: List[str]

class AdapterEventPublish(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionInputList: List[PartitionInputList]
