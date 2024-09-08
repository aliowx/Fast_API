from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix='/blog', tags=['blog'])

class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title: str  # Fixed the typo here
    content: str
    nb_comments: int
    published: Optional[bool] = None
    tags:List[str]
    metadata:Dict[str,str] = {'key1':'value1'}
    image:Image = None



@router.post('/new/{id}')
def create_post(blog: BlogModel, id: int, version: int = 11):
    print(blog.json())  # Fixed json() method
    return {'message': 'OK', 'data': blog, 'id': id, 'version': version}



@router.post('/new/{id}/comment')
def create_comment(
    id: int, 
    blog: BlogModel,  
    comment_id: int = Query(
        None, 
        title='Title Text!', 
        description='Description Text!', 
        alias='CommentID',  
        deprecated=True
    ),
    content: str = Body(
        ..., 
        min_length=10, 
        max_length=20, 
        regex='^[A-Z].*',
    )
):
    return {
        'blog': blog,
        'id': id,
        'comment': comment_id,
        'content': content  # Fixed typo here
    }
