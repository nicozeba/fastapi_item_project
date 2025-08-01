## Item Project - Backend

This project was generated as a simple example of use of FastAPI with a simple CRUD of Item creation.

## Initialize project

### Initialize using UV
**Note:** This is not necessary to do, it's just to inform.

This project uses UV to create the virtual environment

1- Init UV project

```bash
uv init
```

2- Add dependencies

```bash
uv add "fastapi[standard]"
uv add pydantic
```

### Sync the dependencies

If you download the project, you need to sync the dependencies:

```bash
uv sync
```

### Using Virtual Environment

Initialize the virtual enironment
```bash
# Linux / Unix
source .venv/bin/activate

# Windows
.\.venv\Scripts\activate
```

Install the dependencies in `requirements.txt`:
```bash
pythom -m pip install -r requirements.txt
```


## Start the project

Once you install the dependencies you can run the following command to start the backend:

```bash
uv run fastapi dev main.py
```

## Bonus track

### Create requirements.txt using UV

The following command let you create `requirements.txt` file using UV:

```bash
uv pip freeze > requirements.txt
```