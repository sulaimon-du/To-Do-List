from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from db.postgres import engine
from db.models import Task
from logger.logger import logger


def get_all_tasks(user_id):
    with Session(bind=engine) as db:
        db_tasks = db.query(Task).filter(Task.deleted_at == None,
                                         Task.user_id == user_id).all()

        return db_tasks


def get_task_by_id(user_id, task_id):
    with Session(bind=engine) as db:
        db_task = db.query(Task).filter(Task.deleted_at == None,
                                        Task.user_id == user_id,
                                        Task.id == task_id).first()
        if db_task is None:
            logger.error(f"Task {task_id} not found")
            return None

        return db_task


def create_task(task: Task):
    with Session(bind=engine) as db:
        db.add(task)
        db.commit()
        return task.id
