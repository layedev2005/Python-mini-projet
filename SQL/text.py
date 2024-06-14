from sqlalchemy import create_engine

db_path = 'sqlite:///text_alchemy.db'

engine = create_engine(db_path)

try:
    conn = engine.connect()
    print("succes!")


except Exception as ex :
    print(ex)