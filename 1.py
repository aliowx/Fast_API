"""
THis is the project about the test and leant the intern of the some comany actually my daer 
also it's important to use the app and the application to learn something new after that we wanna say 
something about the insomni application , to meake something better we ought to know about the status code http
simular somthing like this 

"""
from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
from fastapi.exceptions import HTTPException

app = FastAPI()


class TypeBlogs(str, Enum):
    Mesal1 = 'mesal1'
    Mesal2 = 'mesal2'
    Mesal3 = 'mesal3'


@app.get("/log/{id}/comments/{comment_id}",tags=['blog','comment'])
async def get_comment(id: int, comment_id: int, valid: bool, username: str):
    return {"id": id, "comment_id": comment_id, "valid": valid, "username": username}

@app.get('/blog/all', tags=['blog'])
def get_blog(page:Optional[int], page_size:str):
    return {'message':f'{page=} -- {page_size}'}


@app.get('/blog/type/{type}')
def get_type_blog(type:TypeBlogs):
    return {'message':f'blog type is {type}'}



@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['aliowx'], summary='Get a blog by ID')
def get_blog_by_id(id: int, response: Response):
    '''
    this is about the API call
    - **id** getting id 
    '''
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Error': f'Blog with ID {id} is not found!'}
    return {'message': f'blog {id}'}