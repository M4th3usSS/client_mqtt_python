# Importa de paho
import paho.mqtt.client as mqtt

# Importa funções de callback
from .callbacks import on_connect, on_subscribe, on_message

class MqttClientConnection:

    # Construtor
    def __init__(self, broker_ip:str, port:int, client_name:str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None

    # Função que inicia a coneção
    def start_connection(self):
        # cliente mqtt
        mqtt_client = mqtt.Client(client_id=self.__client_name)
         
        # Callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message
    
        # Conetaca o cliente MQTT
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        self.__mqtt_client = mqtt_client
        mqtt_client.loop_start()
    
    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            return True
        except:
            return False