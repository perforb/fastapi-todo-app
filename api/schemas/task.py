import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, json_schema_extra={"example": "クリーニングを取りに行く"})
    due_date: datetime.date | None = Field(None, json_schema_extra={"example": "2024-12-01"})


class Task(TaskBase):
    id: int
    done: bool = Field(False, json_schema_extra={"example": "完了フラグ"})

    class ConfigDict:
        from_attributes = True


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskBase):
    id: int

    class ConfigDict:
        from_attributes = True
