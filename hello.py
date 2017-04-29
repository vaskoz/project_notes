from sqlalchemy import create_engine
from flask import Flask
import json
import decimal

app = Flask(__name__)
engine = create_engine('postgresql://localhost:5432/world', echo=True)
connection = engine.connect()

@app.route('/cities')
def list_cities():
    result = connection.execute("select * from city")
    s = json.dumps([dict(r) for r in result])
    return s

@app.route('/countries')
def list_countries():
    result = connection.execute("select name from country")
    s = json.dumps([dict(r) for r in result])
    return s

