from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///Instagram.db", connect_args={"check_same_thread": False})
base = declarative_base()
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()


def run_light_migrations():
    """create_all() never alters existing tables, so add new columns by hand.

    Safe to run on every start-up: a column is only added when it is missing,
    which keeps your existing Instagram.db (users, posts, comments) intact.
    """
    wanted = {
        "user": {"bio": "VARCHAR", "created_at": "DATETIME"},
    }
    with engine.begin() as conn:
        for table, columns in wanted.items():
            existing = {row[1] for row in conn.execute(text(f'PRAGMA table_info("{table}")'))}
            for name, ddl in columns.items():
                if name not in existing:
                    conn.execute(text(f'ALTER TABLE "{table}" ADD COLUMN {name} {ddl}'))
