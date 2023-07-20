from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.blog import BlogCreate, ShowBlog
from db.session import get_db
from db.repository.blogs import create_new_blog, retreive_blog, list_blogs

from typing import List

router = APIRouter()

@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate, db: Session=Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)

    return blog

@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session=Depends(get_db)):
    blogs = list_blogs(db=db)

    return blogs

@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session=Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog