from pydantic import BaseModel
from typing import List, Optional

class Participant(BaseModel):
    name: str
    age: int
    gender: str

class Answer(BaseModel):
    question_id: int
    chosen_answer: str

class ParticipantResult(BaseModel):
    participant_id: int
    answers: List[Answer]
