FROM python:3.8-slim-buster
WORKDIR /reporting
# Install dependencies:
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Run the application:
CMD python app.py
EXPOSE 5002
