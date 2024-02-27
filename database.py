from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://VisitForm_worryalike:9f1d20abcebf8a4cc8daa15fb7b41ac4c71e11ef@6vi.h.filess.io:3307/VisitForm_worryalike",
)


def load_data_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from visitors"))
    data = []
    for row in result.all():
      data.append(dict(row._mapping))
    return data
