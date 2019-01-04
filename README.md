#python_mqtt_sample

This is a python mqtt client sample code to allow to subscribe to the Conduit's MQTT server and echoing/send (publish) the data back to mDot.

Installation:

1. ssh into the Conduit and type the following command to install pip. Make sure your Conduit is connected to the internet.
   
   opkg update

   opkg install python-pip

2. Type: pip install paho-mqtt

3. scp the mqtt-client.py to your Conduit

4. Run it: chmod +x mqtt-client.py

   python mqtt-client.py

 
