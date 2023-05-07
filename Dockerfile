FROM python:3.9

RUN mkdir code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/

EXPOSE 80

WORKDIR /code