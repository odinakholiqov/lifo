from sqlalchemy.orm import Session
from db.repository.blogs import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    blog = CreateBlog(title="test",
                      context="Testing out testing")
    user = create_random_user(db=db)
    blog = create_new_blog(blog=blog, db=db, author_id=user.id)
    
    return blog