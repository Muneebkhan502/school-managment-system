#Get python image from dockerhub
FROM python:3.11
#Set workdir
WORKDIR /app

COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#Copy code
COPY . /app
# Expose port
EXPOSE 8000
#Run the application


CMD uvicorn main:app --host 0.0.0.0 --port $PORT