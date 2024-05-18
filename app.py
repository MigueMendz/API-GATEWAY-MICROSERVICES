from flask import Flask
from infrastructure.routes.routes import orders_bp, order_products_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(orders_bp, url_prefix='/ordenes')
app.register_blueprint(order_products_bp, url_prefix='/ordenes_productos')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
