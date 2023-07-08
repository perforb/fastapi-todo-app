import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="クリーニングを取りに行く")
    due_date: datetime.date | None = Field(None, example="2024-12-01")


class Task(TaskBase):
    id: int
    done: bool = Field(False, example="完了フラグ")

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True
