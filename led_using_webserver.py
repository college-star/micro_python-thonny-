import network
import socket
from machine import Pin

# WiFi credentials (Change these)
SSID = "your hotspot name"
PASSWORD = "your password"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected! IP:", wlan.ifconfig()[0])

# LED Setup (Using GPIO 15)
led = Pin(15, Pin.OUT)

# HTML Webpage
html = """<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <style>
        body {text-align: center; font-family: Arial;}
        button {font-size: 20px; padding: 10px; margin: 10px; cursor: pointer;}
    </style>
</head>
<body>
    <h1>Raspberry Pi Pico LED Control</h1>
    <button onclick="fetch('/led_on')">Turn ON</button>
    <button onclick="fetch('/led_off')">Turn OFF</button>
</body>
</html>
"""

# Web Server
addr = ('', 80)
s = socket.socket()
s.bind(addr)
s.listen(5)

print("Web Server Running...")

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    print(request)

    if "GET /led_on" in request:
        led.value(1)  # Turn LED ON
    elif "GET /led_off" in request:
        led.value(0)  # Turn LED OFF

    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + html)
    conn.close()