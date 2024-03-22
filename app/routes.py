from fastapi import APIRouter, HTTPException
from typing import List
from .models import Participant

router = APIRouter()

@router.post("/participants/", response_model=Participant)
def create_participant(participant: Participant):
    participant.participant_id = 1  # 임시 값으로 1을 할당
    return participant

@router.get("/participants/", response_model=List[Participant])
def get_participants():
    participants = []  # 임시 값으로 빈 리스트를 반환
    return participants
