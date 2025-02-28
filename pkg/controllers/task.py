import json

from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import Response, JSONResponse

from pkg.controllers.middlewares import get_current_user
from pkg.services import task as task_service
from schemas.task import TaskSchema
from logger.logger import logger
from utils.auth import TokenPayload

router = APIRouter()


@router.get("/tasks", summary="Get all tasks", tags=["tasks"])
def get_all_tasks(payload: TokenPayload = Depends(get_current_user)):
    """
        Возвращает все задачи пользователя. Токен авторизации должен быть передан в заголовке.
    """
    user_id = payload.id
    logger.info(f"Get all tasks. Request user: {user_id}")
    tasks = task_service.get_all_tasks(user_id)
    return JSONResponse({"tasks": tasks}, status_code=status.HTTP_200_OK)


@router.get("/tasks/{task_id}", summary="Get task by ID", tags=["tasks"])
def get_task_by_id(task_id: int, payload: TokenPayload = Depends(get_current_user)):
    user_id = payload.id
    if task_id <= 0:
        logger.error(f"Task ID {task_id} is invalid. Request user: {user_id}")
        return JSONResponse({"error": "task_id cannot be negative"}, status_code=status.HTTP_400_BAD_REQUEST)

    task = task_service.get_task_by_id(user_id, task_id)
    if task is None:
        return JSONResponse({"error": "Task not found"}, status_code=status.HTTP_404_NOT_FOUND)
    return task


@router.post("/tasks", summary="Create new task", tags=["tasks"])
def create_task(task: TaskSchema, payload: TokenPayload = Depends(get_current_user)):
    user_id = payload.id
    task_service.create_task(user_id, task)

    return JSONResponse({"message": "Task created"}, status_code=status.HTTP_201_CREATED)


# "1. Добавить новую задачу" +
# "2. Вывести список задач" +
# "4. Вывести задачу по ID" +
# "3. Редактировать задачу" +-
# "5. Удалить задачу по ID" +-
# "6. Пометить задачу Выполнено / Не выполнено" +-
# "7. Корзина (вывод удаленных задач)" +-

@router.put("/tasks/{task_id}", summary="Update task by ID", tags=["tasks"])
def update_task(task_id: int, task: TaskSchema):
    user_id = 1
    return Response(json.dumps({'error': 'not implemented'}), status.HTTP_501_NOT_IMPLEMENTED)


@router.delete("/tasks/{task_id}", summary="Delete task by ID", tags=["tasks"])
def delete_task(task_id: int):
    user_id = 1
    return Response(json.dumps({'error': 'not implemented'}), status.HTTP_501_NOT_IMPLEMENTED)


@router.patch("/tasks/{task_id}/status", summary="Update task status by ID", tags=["tasks"])
def update_task_status(task_id: int, is_done: bool):
    user_id = 1

    return Response(json.dumps({'error': 'not implemented'}), status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/tasks/deleted", summary="Get all deleted tasks", tags=["tasks"])
def get_all_deleted_tasks():
    user_id = 1
    return Response(json.dumps({'error': 'not implemented'}), status.HTTP_501_NOT_IMPLEMENTED)
