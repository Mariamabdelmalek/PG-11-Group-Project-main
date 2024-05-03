from . import orders
from . import order_details
from . import Customers



def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(Customers.router)
