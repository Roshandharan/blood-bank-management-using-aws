from flask import Flask
from backend.routes import donors, inventory, requests

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(donors.bp)
app.register_blueprint(inventory.bp)
app.register_blueprint(requests.bp)

@app.route('/')
def home():
    return "Welcome to Blood Bank Management System"

if __name__ == "__main__":
    app.run(debug=True)
