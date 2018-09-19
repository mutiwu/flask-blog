import json


from flask import Flask
from Config import DevConfig


app = Flask(__name__)

app.config.from_object(DevConfig)


@app.route("/", method="get")
def home():
    retdict = {"ret": "Hello World"}
    return json.dumps(retdict)


if __name__ == "__main__":
    app.run()
