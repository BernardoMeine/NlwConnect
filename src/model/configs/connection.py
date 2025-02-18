from sqlalchemy import create_engine

class DBConnectionHandler:
  def __init__(self):
    self.__connection_string = "sqlite:///schema.db"
    self.__engine = self.__create_database_engine()

  def __create_database_engine(self):
    engine = create_engine(self.__connection_string)
    return engine