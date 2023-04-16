from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)


from app import routes, models

