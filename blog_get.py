from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional
from fastapi.exceptions import HTTPException


router = APIRouter(prefix='/blog',tags=['blog'])


class TypeBlogs(str, Enum):
    Mesal1 = 'mesal1'
    Mesal2 = 'mesal2'
    Mesal3 = 'mesal3'


@router.get("/log/{id}/comments/{comment_id}",tags=['blog','comment'])
async def get_comment(id: int, comment_id: int, valid: bool, username: str):
    return {"id": id, "comment_id": comment_id, "valid": valid, "username": username}

@router.get('/all', )
def get_blog(page:Optional[int], page_size:str):
    return {'message':f'{page=} -- {page_size}'}


@router.get('/type/{type}')
def get_type_blog(type:TypeBlogs):
    return {'message':f'blog type is {type}'}



@router.get('/{id}', status_code=status.HTTP_200_OK, summary='Get a blog by ID')
def get_blog_by_id(id: int, response: Response):
    '''
    this is about the API call
    - **id** getting id 
    '''
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Error': f'Blog with ID {id} is not found!'}
    return {'message': f'blog {id}'}