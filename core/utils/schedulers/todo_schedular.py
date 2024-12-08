from datetime import datetime, timedelta
from typing import Any
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from my_base.core.middlewares.apschedulermw import SchedulerMiddleware

class AsyncScheduler(AsyncIOScheduler):
	store = SQLAlchemyJobStore(url='sqlite:///todo.sqlite', tablename='todo')
	job_stores = {
		'default': store
	}
	job_defaults = {
		'coalesce': False,
		'max_instances': 5
	}
	middleware_scheduler: SchedulerMiddleware
	def __init__(self, *args, **kwargs):
		super().__init__(*args, timezone='Europe/Moscow',
		                  jobstores=self.job_stores, job_defaults=self.job_defaults, **kwargs)
		self.middleware_scheduler = SchedulerMiddleware(self)
	
	def get_middleware_scheduler(self):
		return self.middleware_scheduler

	def add_todo_job(self, func: Any, date: datetime, **kwargs) -> int:
		job_id = int(datetime.now().timestamp())
		self.add_job(func, 'date', run_date=date, kwargs={"job_id": job_id, **kwargs}, id=f"{job_id}")
		return job_id

# async_scheduler = AsyncScheduler()

# async_scheduler.add_job(my_async_function, 'interval', seconds=10,
#                   args=['test text'], id='job_1')

# async_scheduler.add_todo_go(
#       send_todo_go,
#       datetime.now()+timedelta(minutes=5),
#       user_id=375230092,
#       name="test"
#   )