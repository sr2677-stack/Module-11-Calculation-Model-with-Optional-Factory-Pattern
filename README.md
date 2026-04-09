# My Project - Module 11

## Running Tests Locally

```bash
# Start PostgreSQL
docker compose up -d postgres

# Install dependencies
python -m pip install -r requirements.txt

# Unit tests (no DB needed)
python -m pytest tests/unit -v

# Integration tests (needs PostgreSQL)
TEST_DATABASE_URL=postgresql://user:password@localhost:55433/mydb python -m pytest tests/integration -v
```

## Docker Hub
Image: https://hub.docker.com/r/sr2677stack/my_project

Pull and run:
```bash
docker pull sr2677stack/my_project:latest
docker run -p 8000:8000 sr2677stack/my_project
```
