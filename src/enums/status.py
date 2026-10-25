import enum


class StatusType(enum.Enum):
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    PENDING = "pending"
