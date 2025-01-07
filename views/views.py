import __init__
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date


class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        return results

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).where(
                Subscription.empresa == subscription.empresa)
            results = session.exec(statement).all()


ss = SubscriptionService(engine)
# subscription = Subscription(empresa='Pythonando', site='pythonando.com.br', data_assinatura=date.today(), valor=35)
# ss.create(subscription)
print(ss.list_all())
