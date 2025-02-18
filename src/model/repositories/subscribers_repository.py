from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
  def insert(self, subscriber_infos: dict) -> None:
    with DBConnectionHandler() as db:
      try:
        new_subscriber = Inscritos(
          nome=subscriber_infos.get("nome"),
          email=subscriber_infos.get("email"),
          link=subscriber_infos.get("link"),
          evento_id=subscriber_infos.get("evento_id"),
        )
        db.session.add(new_subscriber)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception('Error on insert event')
  
  def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
    with DBConnectionHandler() as db:
      try:
        subscriber = db.session.query(Inscritos).filter_by(email=email, evento_id=evento_id).first()
        return subscriber
      except Exception as exception:
        raise exception('Error on select event')