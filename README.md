# Mini Infrastructure Template

Template project for deploying and monitoring containerized applications.

## Application

The example application is built with:

- Python
- FastAPI
- Uvicorn
- pytest

## Endpoints

### GET /

Returns application greeting.

### GET /health

Application health check.

### GET /info

Returns application information.

## Local development

Create virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:
```bash
uvicorn src.main:app --reload
```
Application will be available at:

`http://127.0.0.1:8000`

Swagger documentation:

`http://127.0.0.1:8000/docs`

## Tests
```bash
pytest
```