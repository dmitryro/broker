FROM python:3.7.5-alpine
 
ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV KAFKA_BOOSTRAP_SERVER_PORT 9092
ENV KAFKA_BOOSTRAP_SERVER_NAME kafka:9092
ENV KAFKA_BROKER kafka://kafka:9092
ENV KAFKA_BOOTSTRAP_SERVER kafka:9092
ENV SCHEMA_REGISTRY_SERVER_PORT 8081
ENV SCHEMA_REGISTRY_SERVER schema-registry:8081

RUN apk update \
    && apk add --no-cache bash git gcc python3-dev musl-dev openssl-dev libffi-dev build-base
# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

COPY . .
RUN chmod +x ./wait_for_services.sh
RUN chmod +x ./run.sh
RUN pip3 install -r requirements.txt

ENTRYPOINT ["./wait_for_services.sh"]

CMD ["./run.sh", "${WORKER}", "${WORKER_PORT}", "${CONFIG_CLASS}"]
