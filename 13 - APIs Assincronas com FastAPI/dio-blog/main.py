from fastapi import FastAPI 
from datetime import datetime, UTC

app = FastAPI()

fake_db= [
    {"title": f"Criando uma aplicação com Django", 'date': datetime.now(UTC), 'published':True},
    {"title": f"Internacionalizando um aoo FastAPI", 'date': datetime.now(UTC),'published':True},
    {"title": f"Criando uma aplicação com Flask", 'date': datetime.now(UTC),'published':True},
    {"title": f"Internacionalizando um aoo Pandas", 'date': datetime.now(UTC),'published':False},
]


@app.get('/posts')
def read_posts(skip:int = 0, limit:int=len(fake_db), published: bool = True):
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]







@app.get('/posts/{framework}')
def read_posts(framework):
    return{
        'posts': [
            {"title": f"Criando uma aplicação com {framework}", 'date': datetime.now(UTC)},
            {"title": f"Internacionalizando um aoo {framework}", 'date': datetime.now(UTC)},
            ]
        }