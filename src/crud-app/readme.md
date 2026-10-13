# FastAPI CRUD App: SQLAlchemy, Pydantic, and Alembic

This example exposes CRUD endpoints for employees. It uses FastAPI for HTTP
handling, SQLAlchemy for database access, Pydantic for request validation and
response serialization, and Alembic for schema migrations.

## Project files

| File or folder | Responsibility |
| --- | --- |
| `database.py` | Defines the database URL, SQLAlchemy engine, session factory, and declarative model base. |
| `models.py` | Defines the SQLAlchemy `Employee` table. |
| `schemas.py` | Defines Pydantic input and output shapes. |
| `crud.py` | Contains database query and mutation functions. |
| `main.py` | Creates the FastAPI app, provides a database dependency, and declares endpoints. |
| `alembic.ini` | Configures Alembic, including its script directory and database URL. |
| `migrations/env.py` | Connects Alembic to the SQLAlchemy model metadata. |
| `migrations/versions/` | Holds the generated, version-controlled migration scripts. |

The model file in this project is named `models.py` (not `model.spy`).

## Install dependencies

From this directory (`src\crud-app`), install the packages used by the app:

```powershell
python -m pip install fastapi "uvicorn[standard]" sqlalchemy alembic "pydantic[email]"
```

`EmailStr` uses Pydantic's email-validation extra. If the project already has a
configured Python environment, activate it before installing or running these
commands.

## 1. Configure the SQLAlchemy connection

`database.py` creates the engine and a factory for database sessions:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "sqlite:///./test.db"

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()
```

- `DB_URL` selects the database. This app uses SQLite and stores `test.db`
  relative to the process's current working directory. Run commands from
  `src\crud-app` to keep the app and Alembic pointed at the same file.
- `engine` manages SQLAlchemy's connection pool. SQLite's
  `check_same_thread=False` setting permits the connection to be used in the
  threaded context typical of this synchronous FastAPI app.
- `SessionLocal` creates a unit-of-work session for a request. `autocommit` is
  disabled so writes are committed explicitly in `crud.py`.
- `Base` is the common parent for ORM models and holds their table metadata.

For another database, install its SQLAlchemy driver and update the URL in both
`database.py` and `alembic.ini` (or configure Alembic to read the URL from the
application settings). Keep the two URLs synchronized.

## 2. Define a table with a SQLAlchemy model

`models.py` defines the database table by inheriting from `Base`:

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
```

`__tablename__` sets the SQL table name. Each `Column` maps an ORM attribute to
a database column; `primary_key`, `unique`, and `index` specify database
constraints or indexes.

The model must be imported before SQLAlchemy or Alembic inspects
`Base.metadata`. Alembic's `migrations/env.py` imports `models` for this reason.

## 3. Define Pydantic schemas

`schemas.py` defines the data accepted from clients and the data returned by
the API:

```python
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    age: Annotated[int, Field(..., gt=0, lt=100)]


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
```

- FastAPI parses and validates a JSON request body against the declared
  Pydantic schema before calling the endpoint. Invalid types, email addresses,
  or ages (age must be greater than 0 and less than 100) result in a validation
  response instead of reaching the CRUD function.
- `EmployeeCreate` and `EmployeeUpdate` are request shapes. They deliberately
  do not let a client supply the database-generated `id`.
- `EmployeeOut` adds `id` for responses. `orm_mode = True` lets Pydantic build
  the response from SQLAlchemy ORM objects rather than requiring a manually
  constructed dictionary.
- `EmployeeUpdate` currently requires every field just like `EmployeeCreate`.
  Therefore, despite using HTTP `PATCH`, the current update route replaces all
  three employee fields; it is not a partial-field update.

This repository uses Pydantic v1-style ORM configuration. In a Pydantic v2
project, use `model_config = ConfigDict(from_attributes=True)` instead of
`class Config: orm_mode = True`.

## 4. Implement database operations

`crud.py` receives an open SQLAlchemy `Session` and performs database work:

```python
def get_all(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=emp.name,
        email=emp.email,
        age=emp.age,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
```

The remaining functions follow the same pattern: retrieve a row, modify or
delete it, and `commit()` the change. `refresh()` reloads a created or updated
object so generated values, such as its primary key, are available to the
response. Keeping these operations outside route functions separates database
access from HTTP handling.

## 5. Create the FastAPI app and inject a database session

`main.py` creates a request-scoped session dependency:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

FastAPI's `Depends(get_db)` calls this function for an endpoint, supplies the
yielded session as the `db` parameter, then resumes the generator and closes
the session after the request completes. The endpoint does not need to open or
close the session itself.

The endpoint declares a Pydantic `response_model` and delegates database work
to `crud.py`. The current routes are:

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/` | List employees |
| `GET` | `/{emp_id}` | Get one employee |
| `POST` | `/create` | Create an employee |
| `PATCH` | `/update/{emp_id}` | Replace an employee's name, email, and age |
| `DELETE` | `/remove/{emp_id}` | Delete an employee |

For reads and writes the data flow is:

1. FastAPI matches the method and path and validates path parameters and body
   data.
2. `Depends(get_db)` provides the request's SQLAlchemy session.
3. The endpoint calls the appropriate function in `crud.py`.
4. SQLAlchemy queries or changes the `employees` table; writes are committed.
5. The endpoint returns the ORM object or list, and `response_model` validates
   and serializes it as JSON.

## 6. Run and try the API

Run from `src\crud-app`, so the SQLite URL resolves to this directory's
`test.db`:

```powershell
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to exercise the endpoints through FastAPI's
interactive API documentation.

Example create request:

```json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "age": 36
}
```

Send it as JSON to `POST http://127.0.0.1:8000/create`. A successful response
includes the generated `id` as well as the submitted fields.

## 7. Manage schema changes with Alembic

Alembic tracks database schema changes as ordered migration scripts. This
project is already initialized: `alembic.ini` points to `migrations/`, and
`migrations/env.py` sets `target_metadata = Base.metadata` after importing the
models. That metadata connection enables `--autogenerate`.

Run Alembic commands from `src\crud-app`:

```powershell
# See the revision currently recorded in the database.
alembic current

# Compare model metadata with the database and create a migration draft.
alembic revision --autogenerate -m "describe the schema change"

# Review and edit the generated script in migrations/versions/ before applying it.

# Apply every migration up to the latest revision.
alembic upgrade head

# Inspect available revisions.
alembic history

# Roll back one revision when appropriate.
alembic downgrade -1
```
Alembic integration

packages:
pip install alembic

How to initate the migration:
	alembic init migrations


this will create a migration folder with eny.py

How to configure the eny.py

1. set the URL
	sqlalchemy.url = sqlite:///./employees.db

2. Import models and base
	from database import Base
	import models
	
3. Set the target meta database
	target_metadata = Base.metadata


How to detect changes and create migration file
	alembic revision --autogenerate -m "add email to employee"

How to fire the DB update
	alembic upgrade head
    
Autogeneration is a starting point, not a substitute for review. Verify the
generated `upgrade()` and `downgrade()` functions, especially for renames,
data migrations, constraints, and changes Alembic cannot infer safely. Commit
the reviewed migration script with the model change so other environments can
apply the same schema transition.

The existing revision
`migrations/versions/274fb3c35ee2_add_age_to_employee.py` adds the `age` column
to an existing `employees` table and removes it on downgrade. Its
`down_revision` is `None`, so it is the first revision in the current migration
history; the migration assumes the table already exists when applied.

### Keep Alembic as the schema authority

`main.py` currently runs `Base.metadata.create_all(bind=engine)` at import
time. `create_all()` can create missing tables, but it does not apply
alterations to existing tables or record migration history. For an
Alembic-managed deployment, remove or disable this call and use
`alembic upgrade head` to create and update the schema. Otherwise, the app may
create a table before Alembic runs, leaving the migration version table and
actual schema out of sync.

The URL in `alembic.ini` (`sqlite:///./test.db`) must refer to the same database
as `DB_URL` in `database.py`. Relative SQLite paths depend on the working
directory, so run both the app and Alembic from this project directory.
