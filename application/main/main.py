# Importa biblioteca interna
import time

# Importa dicionário de configurações do Broker MQTT
from application.configs.broker_configs import mqtt_broker_configs

# Importa função que conecta o cliente MQTT
from .mqtt_connection.mqtt_client_connection import MqttClientConnection

# Função que mantém a conexão com o broker 
def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],
        mqtt_broker_configs["PORT"],
        mqtt_broker_configs["CLIENT_NAME"],
        mqtt_broker_configs["KEEPALIVE"],
    )

    mqtt_client_connection.start_connection()

    while True: time.sleep(0.001)
