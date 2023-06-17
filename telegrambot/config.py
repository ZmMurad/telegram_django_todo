from dotenv import load_dotenv
load_dotenv()
from os import getenv





token=getenv("TOKEN")
url_server_port="http://"+getenv("URL_SERVER")+":"+getenv("PORT")