from pydantic import BaseModel

class Participant(BaseModel):
    name: str
    age: int
    gender: str
    participant_id: int
