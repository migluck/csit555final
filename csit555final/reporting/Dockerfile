FROM python:3.8-slim-buster
WORKDIR /reporting
# Install dependencies:
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
# Run the application:
ENTRYPOINT ["python", "app.py"]
