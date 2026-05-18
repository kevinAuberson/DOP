FROM python:3.12-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for dependency installation
COPY pyproject.toml poetry.lock ./
 
# Install the dependencies
RUN poetry install --no-root

# Copy the pyproject.toml and poetry.lock files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Command to run the application
CMD ["poetry", "run", "uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "80"]