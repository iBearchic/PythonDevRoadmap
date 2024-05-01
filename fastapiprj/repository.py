from database import new_session, TasksORM
from schemas import STask, STaskAdd
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksORM(**task_dict)
            session.add(task)

            # Отправляем запрос до коммита, чтобы автоинкрементом сгенерировать поле id, после чего уже коммитим
            await session.flush()
            await session.commit()

            return task.id



    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksORM)
            res = await session.execute(query)
            task_models = res.scalars().all()
            # Конвертируем возращаемые данные к pydantic схемам
            task_schemas = [STask.model_validate(task) for task in task_models]

            return task_schemas
