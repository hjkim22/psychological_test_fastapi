from fastapi import FastAPI

# FastAPI 애플리케이션 객체 생성
app = FastAPI()

# 라우터 및 모델 등록
from . import routes
