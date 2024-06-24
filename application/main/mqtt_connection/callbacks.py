# Importa dicionário de configurações do Broker MQTT
from application.configs.broker_configs import mqtt_broker_configs

# callback de quando se comunica ao broker
def on_connect(client, userdate, flags, rc):
    if rc == 0:
        print(f"Cliente connectado com sucesso: {client}")
        client.subscribe(mqtt_broker_configs["TOPIC"])
    else:
        print(f"Erro ao conectar: código={rc}")

# callback de quando se inscreve no broker
def on_subscribe(client, userdate, mid, granted_qos):
    print(f"Cliente Subscribed at {mqtt_broker_configs["TOPIC"]}")
    print(f"QOS: {granted_qos}")

# callback de quando uma messagem é recebida no tópico inscrito
def on_message(client, userdate, message):
    print("Mensagem recebida!")
    print(client)
    print(message.payload)