FROM python:3.8-slim-buster
WORKDIR /tax_calculation
# Install dependencies:
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Run the application:
CMD python app.py
EXPOSE 5000
