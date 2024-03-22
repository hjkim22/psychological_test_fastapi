# 기본 이미지로 Python 3.9를 선택합니다.
FROM python:3.9

# 환경 변수 설정으로 Python이 stdout에 출력하도록 합니다.
ENV PYTHONUNBUFFERED=1

# 작업 디렉터리 설정
WORKDIR /app

# poetry 설치
RUN pip install --upgrade pip \
  && pip install poetry

# pyproject.toml 파일과 poetry.lock 파일(있는 경우) 복사
COPY pyproject.toml poetry.lock* ./

# 종속성 설치
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# 애플리케이션 복사
COPY . .

# FastAPI 애플리케이션 실행을 위한 환경 변수 설정
ENV APP_MODULE=app:create_app
ENV PORT=8000

# uvicorn으로 앱 실행
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app:create_app()"]
