from app import db
from app.models import Task, Post
from app.scrapers import jsonplaceholder

def set_up():
    db.drop_all()
    db.create_all()

def create_tasks():
    t1 = Task(title='Task 1')
    t2 = Task(title='Task 2')
    t3 = Task(title='Task 3')
    t4 = Task(title='Task 4')
    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(t4)
    
    db.session.commit()


def import_posts():
    status_code, json_data = jsonplaceholder.fetch_posts()
    if status_code == 200:
        for jd in json_data:
            title = jd['title']
            p = Post(id=jd['id'], title=title, body=jd['body'])
            db.session.add(p)
            print(f'Fetched {title}')
        db.session.commit()


if __name__ == '__main__':
    set_up()
    create_tasks()
    import_posts()
