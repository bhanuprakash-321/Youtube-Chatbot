# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY htmlTemplates.py .

# Expose Streamlit port
EXPOSE 8501

# Streamlit headless mode
ENV STREAMLIT_SERVER_HEADLESS true

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
