from dagster import ScheduleDefinition
from ..jobs import movies_job

movies_schedule = ScheduleDefinition(
    job = movies_job,
    cron_schedule="0 0 * * 1", # “At 00:00 on Monday.”
)