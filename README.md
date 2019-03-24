# Kafka hello world
***
After looking for a while for a hello world project for Kafka, I only found older versions or ones that did not work. 
I wanted to create one for referece that was interesting and simple.
***

### Intro & Setup
This was done with homebrew on Mac using the latest versions of Kafka and Zookeeper as of 2019-03-24

**Step 1:**

- install packages

~PIP packages installed~
pip install Flask

~Home Brew packages installed~
brew install kafka
brew install zookeeper

**Step 2:**

- create directory for the files or clone this repo

mkdir Kafka
cd Kafka
touch producer.py
touch consumer.py

**Step 3:**
Start Kafka and Zookeeper with Brew Services
