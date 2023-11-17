FROM python:3.13-rc

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
