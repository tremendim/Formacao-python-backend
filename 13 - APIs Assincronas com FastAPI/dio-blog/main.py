from fastapi import FastAPI , status
from datetime import datetime, UTC
from pydantic import BaseModel

app = FastAPI()

fake_db= [
    {"title": f"Criando uma aplicação com Django", 'date': datetime.now(UTC), 'published':True},
    {"title": f"Internacionalizando um aoo FastAPI", 'date': datetime.now(UTC),'published':True},
    {"title": f"Criando uma aplicação com Flask", 'date': datetime.now(UTC),'published':True},
    {"title": f"Internacionalizando um aoo Pandas", 'date': datetime.now(UTC),'published':False},
]


class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False



@app.post('/posts',status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get('/posts')
#def read_posts(skip:int = 0, limit:int=len(fake_db), published: bool = True):
 #   return [post for post in fake_db[skip: skip + limit] if post['published'] is published]
def read_posts(published:bool, limit: int, skip: int=0):
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] is published:
            posts.append(post)
        
    return posts






@app.get('/posts/{framework}')
def read_posts(framework):
    return{
        'posts': [
            {"title": f"Criando uma aplicação com {framework}", 'date': datetime.now(UTC)},
            {"title": f"Internacionalizando um aoo {framework}", 'date': datetime.now(UTC)},
            ]
        }