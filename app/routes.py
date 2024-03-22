from fastapi import HTTPException, APIRouter, Request, Form, Response, Cookie
from fastapi.templating import Jinja2Templates
from .models import Participant, ParticipantResult
from typing import List, Dict

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

participants_db: Dict[int, Participant] = {}
answers_db: Dict[int, List[ParticipantResult]] = {}

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/participants")
async def add_participant(participant: Participant, response: Response):
    participant_id = len(participants_db) + 1
    participants_db[participant_id] = participant
    return {"redirect": "/question", "participant_id": participant_id}

@router.get("/question")
async def question(request: Request):
    return templates.TemplateResponse("question.html", {"request": request})

@router.post("/submit")
async def submit(participant_id: int, answers: List[ParticipantResult], response: Response):
    if participant_id not in participants_db:
        raise HTTPException(status_code=404, detail="Participant not found")
    
    if participant_id not in answers_db:
        answers_db[participant_id] = []

    answers_db[participant_id].extend(answers)
    return {"message": "Answers submitted successfully."}

@router.get("/results")
async def results(request: Request):
    return templates.TemplateResponse("results.html", {"request": request, "participants_db": participants_db, "answers_db": answers_db})
