from sqlalchemy.orm import Session

from schemas.blog import BlogCreate, ShowBlog

from db.models.blog import Blog


def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):

    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog
 
def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()

    return blog 