from flask import Flask, Response
from kafka import KafkaConsumer,TopicPartition
import numpy as np
from PIL import Image
import cv2
import time
from io import BytesIO

#connect to Kafka server and pass the topic we want to consume
kafka_broker = 'g01-01:9092'
consumer = KafkaConsumer('input', group_id='test-consumer-group', bootstrap_servers='g01-01:9092')

app = Flask(__name__)

@app.route('/')
def index():
    # return a multipart response
    return Response(kafkastream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def kafkastream():

    for msg in consumer:
        print('start playing...')
        print(len(msg), len(msg.value))
        print(type(msg.value))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + msg.value + b'\r\n\r\n')

						


if __name__ == '__main__':
	app.run(host="10.244.1.12",debug=True,port=54321)
        
