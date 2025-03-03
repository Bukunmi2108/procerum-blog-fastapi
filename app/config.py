
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .settings import settings

uri = f"mongodb+srv://bukunmi:{settings.password}@procerum-blog.xxwan.mongodb.net/?retryWrites=true&w=majority&appName=procerum-blog"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Procerum
blogs_collection = db["blogs"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)