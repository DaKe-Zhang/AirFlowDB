from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'neozhang',
}

with DAG(
    dag_id='executing_multiple_tasks',
    description='DAG with multiple tasks and dependencies',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@once'
) as dag:
    
    taskA=BashOperator(
        task_id='taskA',
        bash_command='echo TASK A has executed!'
    )

    taskB=BashOperator(
        task_id='taskB',
        bash_command='echo TASK B has executed!'
    )

    taskC=BashOperator(
        task_id = 'taskC',
        bash_command='''
            echo TASK C has started
            sleep 15
            echo TASK C has ended!
        '''
    )

    taskD=BashOperator(
        task_id='taskD',
        bash_command='echo TASK D completed!'
    )

taskA >> [taskB, taskC]

taskD << [taskB, taskC]




