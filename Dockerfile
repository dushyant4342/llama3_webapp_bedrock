# Use Amazon Linux base image
FROM amazonlinux:2023

# Set working directory
WORKDIR /app

# Copy files from GitHub repo
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app (This ensures that when the container starts, it automatically runs the Streamlit app.)
CMD ["streamlit", "run", "llama3.py", "--server.port=8501", "--server.address=0.0.0.0"]


