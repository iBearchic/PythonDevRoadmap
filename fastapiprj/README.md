# Simple application to process user messages

## FASTAPI sample

### Stack:
* FastAPI
* asyncio
* SQLAlchemy

### Main steps:
* python3 -m venv venv
* pip3 install fastapi uvicorn pydantic aiosqlite sqlalchemy
* uvicorn main:app --reload
* docker build . --tag faprj && docker run -p 80:80 faprj
