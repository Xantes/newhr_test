FROM python:3.12.2-alpine3.18

WORKDIR /code

COPY . .

RUN pip install -r requirements.cfg

ENTRYPOINT [ "python", "app.py" ]