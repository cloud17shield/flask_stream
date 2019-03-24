from kafka import KafkaProducer

#  connect to Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Assign a topic
topic = 'test-topic-1'

# Hipsum paragraph as an example set of text data to stream
message_data = "Lorem ipsum dolor amet lo-fi venmo knausgaard, roof party activated charcoal franzen prism mlkshk subway tile williamsburg jean shorts waistcoat cold-pressed. Sriracha microdosing pug squid deep v, you probably haven't heard of them swag try-hard pok pok snackwave quinoa actually shaman selfies hashtag. Twee tofu copper mug, kickstarter butcher cred glossier. Selfies bespoke woke kale chips kickstarter biodiesel edison bulb vice normcore, irony fam. Subway tile marfa asymmetrical squid yr meh next level. Kafka Stream data complete. <hr><br>".split(" ")

def message_emitter(message_data):
    print("Beginning Message Kafka Stream")
    msg_num = 1
    for msg in message_data:
        # encode the key and value as bytes before sending
        producer.send(topic, 
            key=bytes(str(msg_num), 'utf-8'),  
            value=bytes(msg, 'utf-8')).get(timeout=60)
        
        msg_num +=1
        
    print("Emit complete")


if __name__ == "__main__":
	message_emitter(message_data)
