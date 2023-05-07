# global-emissions
Global emissions API


FastAPI local development:
1. Run `uvicorn main:app --reload`
2. Open browser: http://127.0.0.1:8000/

Docker setup
1. `docker build . -t ge`
2. `docker run --rm -it  -p 80:80/tcp ge:latest`
3. Open browser: `http://localhost`


Docker compose
1. `docker compose up --build -d` - rebuilds the docker image and brings it up in detached mode
2. `docker compose stop` - shuts down the service container