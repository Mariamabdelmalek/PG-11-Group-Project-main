from . import orders, order_details, recipes, sandwiches, resources, Customers,Payments, PromotionApplied, Reviews, MenuItems

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    Customers.Base.metadata.create_all(engine)
    Payments.Base.metadata.create_all(engine)
    Promotion.Base.metadata.create_all(engine)
    PromotionApplied.Base.metadata.create_all(engine)
    Reviews.Base.metadata.create_all(engine)
    MenuItems.Base.metadata.create_all(engine)


