from kafka import KafkaProducer
import csv

def kafka_connect_serveur() -> None:
    """"""

    kafka_bootstrap_servers = ':29092'
    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

    return producer

def kafka_send_data() -> list:

    producer = kafka_connect_serveur()
    kafka_topic = 'mytopic'
    
    csvfile = ''

    with open(csvfile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  

        for row in csv_reader:
            nom = row[0]
            prenom = row[1]
            numero = row[2]

            row_ = ','.join(row)

            producer.send(kafka_topic, value=row_.encode('utf-8'))

    producer.close()

