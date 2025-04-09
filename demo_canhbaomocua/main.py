from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_button import GroveButton
import time
import paho.mqtt.client as mqtt
import json

# Kết nối CounterFit
CounterFitConnection.init("127.0.0.1", 5000)

# Khai báo thiết bị
light_sensor = GroveLightSensor(0)
button = GroveButton(2)
led = GroveLed(4)

# Kết nối MQTT Broker
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()

print("Hệ thống cảnh báo cửa mở đang chạy...\n")

while True:
    # Đọc dữ liệu từ cảm biến
    light = light_sensor.light
    door_opened = button.is_pressed()

    # Hiển thị trạng thái
    print(f"Ánh sáng: {light:.2f} lux | Cửa mở: {'Có' if door_opened else 'Không'}")

    # Xử lý cảnh báo
    if door_opened:
        print("\n>>> CẢNH BÁO: CỬA ĐANG MỞ! <<<\n")
        led.on()
    else:
        led.off()

    # Gửi dữ liệu qua MQTT
    payload = {
    "light": light,
    "door_open": door_opened
    }
    mqtt_client.publish("iot/canhbao", json.dumps(payload))
    print("📤 Sending payload:", json.dumps(payload))

    print(f"Ánh sáng: {light:.2f} lux | Cửa mở: {'Có' if door_opened else 'Không'}")

    if door_opened:
        print("\n>>> CẢNH BÁO: CỬA ĐANG MỞ! <<<\n")
        led.on()
    else:
        led.off()

    time.sleep(1)

