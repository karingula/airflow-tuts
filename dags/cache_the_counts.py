from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'karingula',
    'depends_on_past': False,
    'start_date': datetime(2019, 8, 13),
    'end_date': None,
    'retries': 2,
    'email_on_failure': False,
    'retry_delay': timedelta(minutes=1)
}

dags = DAG('cache_dag', default_args=args)


def print_context(val):
    print(val)


def print_text():
    print('Hello-World!')


t1 = PythonOperator(
    task_id='multitask1',
    op_kwargs={'val': {'a': 1, 'b': 2}},
    python_callable=print_context, dag=dags)
t2 = PythonOperator(
    task_id='multitask2',
    python_callable=print_text,
    dag=dags)

# t2 will depend on t1
t2.set_upstream(t1)
