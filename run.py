from flask import Flask
from web import op
app = Flask(__name__)
app.register_blueprint(op)

app.config["SECRET_KEY"] = "12345678"

if __name__=='__main__':
    app.run(host='0.0.0.0',
            debug=True,
            port=8879
            )