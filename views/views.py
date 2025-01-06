import __init__
from models.database import engine
from models.model import Subscription


class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        ...


ss = SubscriptionService(engine)
subscription = Subscription('netflix', 'netflix.com.br', '12/12/2024', 25)
ss.create(subscription)
