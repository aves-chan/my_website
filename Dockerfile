FROM python:3.11

WORKDIR /my_website

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/backend/main.py"]

LABEL authors="aves-chan"