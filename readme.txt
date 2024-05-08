pip install update

python --version
echo $AIRFLOW_HOME
export AIRFLOW_HOME=/workspaces/AirFlowDB/airflow

AIRFLOW_VERSION=2.9.1
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"


airflow db migrate 

airflow users list

airflow users create \
>           --username admin \
>           --firstname FIRST_NAME \
>           --lastname LAST_NAME \
>           --role Admin \
>           --email admin@example.org \
>           --password password!

