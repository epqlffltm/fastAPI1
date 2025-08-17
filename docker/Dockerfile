# 파이썬 3.11 이미지 다운로드
FROM python:3.11-buster

# 파이썬 출력표시를 Docker용으로 조정
ENV PYTHONUNBUFFERED=1

# 소스 코드를 위한 작업 디렉토리 설정
WORKDIR /src

# pip로 poetry 설치
RUN pip install "poetry==1.6.1"

# poetry 정의 파일 복사 (존재하는 경우)
COPY pyproject.toml poetry.lock ./

# poetry로 라이브러리 설치
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# 애플리케이션 실행
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
