from enum import IntEnum
from dataclasses import dataclass


class MaintenanceCommand(IntEnum):
    SuspendMemPool = 0,
    ResumeMemPool = 1,
    Dummy = -1


@dataclass
class MaintenanceRequest:
    command: MaintenanceCommand = MaintenanceCommand.Dummy
    req_id: str = ""
