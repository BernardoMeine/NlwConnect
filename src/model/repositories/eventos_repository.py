from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
  def insert(self, event_name: str) -> None:
    with DBConnectionHandler() as db:
      try:
        new_event = Eventos(nome=event_name)
        db.session.add(new_event)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception('Error on insert event')

  def select_event(self, event_name: str) -> Eventos:
    with DBConnectionHandler() as db:
      try:
        event = db.session.query(Eventos).filter_by(nome=event_name).first()
        return event
      except Exception as exception:
        raise exception('Error on select event')