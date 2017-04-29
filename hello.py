from sqlalchemy import create_engine
from flask import Flask
app = Flask(__name__)
engine = create_engine('postgresql://localhost:5432/cities', echo=True)
connection = engine.connect()

@app.route('/')
def hello_world():
    result = connection.execute("select name from city")
    s = ""
    for row in result:
        s += row['name']
        s += "\n"
    connection.close()
    return s

