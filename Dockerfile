FROM python:3.11-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=mockapp_fintech.settings \
    PORT=8000

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create directory for static files
RUN mkdir -p /app/staticfiles

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Create a non-root user
RUN adduser --disabled-password --gecos '' webuser
RUN chown -R webuser:webuser /app
USER webuser

# Make port 8000 available
EXPOSE 8000

# Add startup script
COPY startup.sh /app/startup.sh
RUN chmod +x /app/startup.sh

# Use the startup script as entrypoint
ENTRYPOINT ["/app/startup.sh"]