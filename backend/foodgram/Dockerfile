FROM python:3.9-slim

RUN mkdir /app
COPY . .
RUN pip3 install -r ./requirements.txt --no-cache-dir && python -m pip install --upgrade pip

COPY . /app

WORKDIR /app

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ] 