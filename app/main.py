from fastapi import FastAPI
from .schema import Blog, UpdateBlog
from .config import blogs_collection
from .serializer import *
from bson import ObjectId
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/blogs")
def get_blogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)
    return decoded_data

@app.get("/blogs/{_id}")
def get_blogs(_id: str):
    res = blogs_collection.find_one({"_id": ObjectId(_id)})
    
    decoded_data = DecodeBlog(res)
    return decoded_data

@app.post("/blogs/create")
def create_blog(blog: Blog):
    blog = dict(blog)
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    blog['date'] = str(current_date)
    blog['time'] = str(current_time)
    
    res = blogs_collection.insert_one(blog)
    blog_id = str(res.inserted_id)
    return {
        "status": "ok",
        "message": "Blog created succesfully",
        "_id": blog_id
    }

@app.patch("/blogs/{_id}/update")
def update_blog(_id: str, blog: UpdateBlog):    
    req = dict(blog.model_dump(exclude_unset=True))
    blogs_collection.find_one_and_update(
        {"_id": ObjectId(_id)},
        {"$set": req}
        )
    
    return {
        "status": "ok",
        "message": "Blog updated successfully"
    }

@app.delete("/blogs/{_id}/delete")
def create_blog(_id: str):
    blogs_collection.find_one_and_delete({"_id": ObjectId(_id)})
    
    return {"message": "Blog deleted"}

