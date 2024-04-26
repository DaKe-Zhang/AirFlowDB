# AirFlowDB
AirFlowDB

# installation
export AIRFLOW=/workspaces/AirFlowDB
export AIRFLOW_HOME=/workspaces/AirFlowDB

AIRFLOW_VERSION=2.9.0

PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"