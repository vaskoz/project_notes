from sqlalchemy import create_engine
from flask import Flask
import json

app = Flask(__name__)
engine = create_engine('postgresql://localhost:5432/cities', echo=True)
connection = engine.connect()

@app.route('/')
def hello_world():
    result = connection.execute("select name from city")
    s = json.dumps([dict(r) for r in result])
    return s

