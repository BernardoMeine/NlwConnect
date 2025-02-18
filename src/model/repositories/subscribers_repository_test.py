import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
  subscriber_info = {
    "nome": "Joel",
    "email": "joelito@email.com",
    "evento_id": 1
  }
  subs_repo = SubscribersRepository()
  subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select  in DB")
def test_select():
  email = "joelito@email.com"
  evento_id = 1

  subs_repo = SubscribersRepository()
  res = subs_repo.select_subscriber(email, evento_id)
  print(res.email)

