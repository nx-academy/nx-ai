FROM python:3.13

WORKDIR /workspaces/nx-ai
COPY . .

RUN pip install -r requirements.txt

