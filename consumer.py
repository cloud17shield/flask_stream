from flask import Flask, Response
from kafka import KafkaConsumer, TopicPartition
import numpy as np
from PIL import Image
import cv2
import time
from io import BytesIO

# connect to Kafka server and pass the topic we want to consume
brokers = "G01-01:2181,G01-02:2181,G01-03:2181,G01-04:2181,G01-05:2181,G01-06:2181,G01-07:2181,G01-08:2181," \
          "G01-09:2181,G01-10:2181,G01-11:2181,G01-12:2181,G01-13:2181,G01-14:2181,G01-15:2181,G01-16:2181 "

consumer = KafkaConsumer('output', group_id='test-consumer-group', bootstrap_servers='g01-01:9092')

app = Flask(__name__)


@app.route('/')
def index():
    # return a multipart response
    return Response(kafka_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def kafka_stream():
    for msg in consumer:
        print('start playing...')
        print(len(msg), len(msg.value))
        print(type(msg.value))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + msg.value + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host="10.244.1.12", debug=True, port=54321)
