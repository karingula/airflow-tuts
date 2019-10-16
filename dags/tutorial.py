# DAG definition file

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

#Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 8, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'queue': 'bash_queue',
    'pool': 'backfill',
    'priority_weight': 10,
    'end_date': datetime(2019, 12, 12)
}

# Instantiating a DAG
dag = DAG('tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

# Tasks
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

# Templating with Jinja
templated_command = """
    {% for in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7) }}"
        echo "{{ params.my_param }}"
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t1.set_downstream(t2)
t1.set_downstream(t3)
# print('DAG')
