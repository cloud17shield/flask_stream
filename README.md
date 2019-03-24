# Kafka hello world
***
After looking for a while for a hello world project for Kafka, I only found older versions or ones that did not work. 
I wanted to create one for referece that was interesting and simple.
***

### Intro & Setup
This was done with homebrew on Mac using the latest versions of Kafka and Zookeeper as of 2019-03-24

**Step 1: install packages**

##### PIP packages installed
pip install Flask

##### Home Brew packages installed
brew install kafka

brew install zookeeper

**Step 2: create directory for the files or clone this repo**

mkdir Kafka
cd Kafka
touch producer.py
touch consumer.py

**Step 3: start Kafka and Zookeeper with Brew Services**
brew services start kafka
brew services start zookeeper

- to check running services use: 'brew services list'


**Step 4: run the consumer.py file**
While in the Kafka directory created above, run 'python consumer.py'.
This should start the flas site and prepare Kafka consumer for receiving data.


**Step 5: open flask site**

Navigate to 0.0.0.0:5000 in your browser.
Should see Hipsum Kafka Stream Data: header

**Step 6: start producer to send data**

In another terminal whie in the Kafka directory created above, run producer.py
can be run a few times to see another group of text being rendered on the Flask site.


The last step should emit the data and you should begin to see the Flask page rendering the messages.
The producer file splits the entire text string on spaces and sends each as a message.
The Flask site and consumer.py file applies a .05 second delay while rendering but uses a generator to keep rendering.
Try running the consumer
