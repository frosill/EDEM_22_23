FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

COPY requirements.txt .
COPY edem_dataflow_streaming_sol.py .
COPY bq_schema.json schema/

# Do not include `apache-beam` in requirements.txt
ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="${WORKDIR}/requirements.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/edem_dataflow_streaming_sol.py"

# Install apache-beam and other dependencies to launch the pipeline
RUN pip install apache-beam[gcp]
RUN pip install -U -r ./requirements.txt