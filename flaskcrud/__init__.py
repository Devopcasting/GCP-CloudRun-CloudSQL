from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.cloud import secretmanager
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'

# GCP Secret Manager
client = secretmanager.SecretManagerServiceClient()
requests = "projects/841764382700/secrets/flaskcrud-secret/versions/1"
response = client.access_secret_version({"name":requests})
secret_dict = json.loads(response.payload.data.decode("utf-8"))

dbUsername = secret_dict["dbUsername"]
dbPassword = secret_dict["dbPassword"]
dbName = secret_dict["dbName"]
dbHost = secret_dict["dbHost"]
dbInstance = secret_dict["dbInstance"]
instanceUnixSocket = secret_dict["instanceUnixSocket"]
dbPort = 3306

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}?unix_socket={instanceUnixSocket}"
app.config["SQLALCHEMT_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from flaskcrud.home.routes import homeBlueObj
from flaskcrud.add.routes import addBlueObj
from flaskcrud.update.routes import updateBlueObj

app.register_blueprint(home.routes.homeBlueObj,url_prefix='/')
app.register_blueprint(add.routes.addBlueObj,url_prefix='/add')
app.register_blueprint(update.routes.updateBlueObj,url_prefix='/update')
