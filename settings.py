SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
    'REQUIRED_SETTINGS': ('KAFKA_BOOTSTRAP_SERVER',),
}

# The following variables can be ovirriden from ENV
KAFKA_BROKER = "kafka://kafka:9092"
KAFKA_BOOTSTRAP_SERVER = "kafka:9092"
KAFKA_BOOSTRAP_SERVER_NAME = "kafka:9092"
KAFKA_BOOSTRAP_SERVER_PORT = 9092
SCHEMA_REGISTRY_URL = "http://schema-registry:8081"
SCHEMA_REGISTRY_SERVER_PORT = 8081
SCHEMA_REGISTRY_SERVER = "schema-registry:8081"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'example': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
