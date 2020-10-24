FROM python:3.6-buster
WORKDIR /app/
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY . .

CMD ["python", "./main.py"]