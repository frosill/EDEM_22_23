from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.branch import BaseOperator
from datetime import datetime
import datetime

with DAG(
    dag_id="sample_dag",
    start_date=datetime.datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end', trigger_rule="ALL DONE")
    true_task = EmptyOperator(task_id='true_task')
    false_task = EmptyOperator(task_id='false_task')

    @task.branch(task_id="is_saturday")
    def is_saturday():
        if datetime.today().isoweekday() == 6:
            return "true_task"
        return "false_task"

    
    # Here the DAG dependencies
    start >> is_saturday() >> [true_task, false_task] >> end
