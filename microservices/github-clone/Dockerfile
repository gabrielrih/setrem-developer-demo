FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app
ADD ./requirements/common.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt update
RUN apt install git -y

COPY ./src /app/src
COPY main.py /app

CMD ["python", "main.py"]
