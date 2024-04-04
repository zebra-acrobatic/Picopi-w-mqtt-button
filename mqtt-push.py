import time
from machine import Pin
import network
from umqtt.simple import MQTTClient

Button = Pin(18, Pin.IN)
 
# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)  # STA_IF for station mode (client)
wifi.active(True)
wifi.connect(SSID, Password)  # Replace 'SSID' and 'password' with your Wi-Fi credentials

# Wait until connected
while not wifi.isconnected():
    pass
print('Connected to Wi-Fi:', wifi.ifconfig())

mqtt_client_id = "somethingreallyrandomandunique123"

mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server="test.mosquitto.org",
        user="",
        password="")

mqtt_client.connect()

# Main Loop
while True:

  # Sleep to improve performance
  time.sleep(0.1)

  # Check if the button was pressed
  if Button.value() == 1:
    print("Hello, Pi Pico!")
    mqtt_client.publish("bob", "Hello")
    time.sleep(0.3)
