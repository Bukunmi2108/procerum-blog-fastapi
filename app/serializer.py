#Decode blog

def DecodeBlog(blog) -> dict:
    return{
        "_id": str(blog["_id"]),
        "title": blog["title"],
        "subheading": blog["subheading"],
        "content": blog["content"],
        "author": blog["author"],
        "tags": blog["tags"],
        "date": str(blog["date"]),
        "time": str(blog["time"])
    }


# all blogs

def DecodeBlogs(blogs) -> list:
    return [
        DecodeBlog(blog) for blog in blogs
    ]