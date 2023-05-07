# global-emissions
Global emissions API


FastAPI local development:
1. Run `uvicorn main:app --reload`
2. Open browser: http://127.0.0.1:8000/

Docker setup
1. `docker build . -t uvicorn`
2. `docker run --rm -it  -p 80:80/tcp uvicorn:latest`
