FROM python:3.10.16
COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 8989

CMD ["python", "orchestrator.py"]

