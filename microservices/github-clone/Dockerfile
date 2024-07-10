FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt update
RUN apt install git -y

COPY ./src /app

CMD ["python", "main.py"]
