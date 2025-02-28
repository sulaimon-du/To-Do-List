
import uvicorn
from fastapi import FastAPI

from configs.config import settings
from pkg.controllers.task import router as task_router
from pkg.controllers.user import router as user_router
from pkg.controllers.auth import router as auth_router
from db.models import migrate_tables

if __name__ == "__main__":
    # Создание таблиц
    migrate_tables()

    # Создание роутера
    app = FastAPI()
    # Подключаем маршруты
    app.include_router(auth_router)
    app.include_router(task_router)
    app.include_router(user_router)

    uvicorn.run(app, port=settings.port, host=settings.host)
# Задача:
# Название - title
# Описание - description
# Срок выполнения - deadline
# Приоритет - priority (низкий, средний, высокий)
# Статус - is_done

from console_application import ConsoleApplication
from db import migrate_tables, close_db_conn

try:
    migrate_tables()

    c = ConsoleApplication()
    c.start()
    close_db_conn()
except Exception as e:
    print("Произошла ошибка: ", e)
    exit(1)
