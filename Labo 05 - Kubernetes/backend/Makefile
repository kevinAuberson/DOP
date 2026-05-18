BACKEND_DIR = backend
FRONTEND_DIR = frontend

# Install dependencies for backend and frontend
install:
    @echo "Installing backend dependencies..."
    cd $(BACKEND_DIR) && poetry install
    @echo "Installing frontend dependencies..."
    cd $(FRONTEND_DIR) && npm install

# Start backend in development mode
dev-backend:
    @echo "Starting backend in development mode..."
    cd $(BACKEND_DIR) && poetry run uvicorn src.backend.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend in development mode
dev-frontend:
    @echo "Starting frontend in development mode..."
    cd $(FRONTEND_DIR) && npm run dev

# Start only the database
dev-database:
    @echo "Starting database..."
    docker-compose up database