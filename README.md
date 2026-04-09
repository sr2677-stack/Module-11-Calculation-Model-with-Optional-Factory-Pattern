# My Project — Module 11

## Running Tests Locally

```bash
# Start PostgreSQL
docker-compose up -d db

# Install dependencies
pip install -r requirements.txt

# Unit tests (no DB needed)
pytest tests/unit -v

# Integration tests (needs PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/mydb pytest tests/integration -v
```

## Docker Hub
Image: https://hub.docker.com/r/YOUR_USERNAME/my_project

Pull and run:
```bash
docker pull YOUR_USERNAME/my_project:latest
docker run -p 8000:8000 -e DATABASE_URL=... YOUR_USERNAME/my_project:latest
```