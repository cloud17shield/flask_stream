from flask import Flask, Response
from kafka import KafkaConsumer
import time

#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('test-topic-1', 
	bootstrap_servers=['localhost:9092'],
	group_id='my-group')

app = Flask(__name__)

@app.route('/')
def index():	
	return Response(kafkastream())


def kafkastream():
	print("Ready to recv messages...")
	yield "<h2>Hipsum Kafka Stream Data:</h2><br>"
	for msg in consumer:
		yield f"{msg.value.decode('utf-8')} "

		# can use below sleep to delay how quickly the messages are rendered
		time.sleep(0.05)
	yield "<hr>"


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)