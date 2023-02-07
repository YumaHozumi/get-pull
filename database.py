from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./pullreq.db"

# connect_argsはSQLiteのみに必要
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# DeclarativeでマッピングされるDBテーブルを記述するためのクラスを作成することができる
Base = declarative_base()
# test