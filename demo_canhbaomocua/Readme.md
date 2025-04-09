# Hệ thống cảnh báo cửa mở - IoT Project

##  Yêu cầu
- Python 3.10+
- Môi trường ảo: `python -m venv counterfit_env`
- Kích hoạt: `counterfit_env\Scripts\activate`
- Cài đặt module:
    pip install -r requirements.txt

##  Thiết bị mô phỏng (CounterFit)
- LED cảnh báo (D4)
- Grove Light Sensor (A0)
- Grove Button (D2)

##  Tích hợp hệ thống
- Platform: Mainflux (chạy Docker đã setup ổn)
- Giao tiếp: Có thể tích hợp thêm HTTP/MQTT gửi dữ liệu đến Mainflux hoặc hiển thị dashboard riêng (tuỳ nâng cấp).

#  Đồ án IoT – Hệ thống cảnh báo cửa mở (CounterFit + MQTT + Mainflux)

##  Mô tả
Hệ thống cảnh báo khi phát hiện cửa bị mở, 
sử dụng các thiết bị cảm biến giả lập bằng phần mềm CounterFit. 
Dữ liệu được truyền thông qua giao thức **MQTT**, lưu trữ bằng **InfluxDB** và hiển thị trên **Grafana**. Hệ thống triển khai bằng **Docker Compose**.

---

## 🛠️ Thành phần chính

| Thành phần | Mô tả |
|------------|-------|
| `CounterFit` | Giả lập phần cứng IoT trên Windows |
| `Mosquitto MQTT Broker` | Giao tiếp dữ liệu từ thiết bị |
| `Telegraf` | Nhận dữ liệu MQTT, ghi vào InfluxDB |
| `InfluxDB` | Cơ sở dữ liệu time-series |
| `Grafana` | Hiển thị dữ liệu dưới dạng biểu đồ |

---

# Cấu trúc thư mục
iot-canhbaomocua
|- counterfit 
|- mainflux 0.21.0 ── docker --> docker-compose 
|- telegraf --\ telegraf.conf # Đọc dữ liệu từ MQTT, gửi vào InfluxDB 
|- counterfit_env 
|- iot_canh_bao_demo --\main.py # Chạy hệ thống cảnh báo
                        └── requirements.txt # Các thư viện cần cài
                        └── README.md

---

#  1. Cài đặt thư viện Python (CounterFit)

Tạo môi trường ảo (nếu cần):
```bash
python -m venv counterfit_env
counterfit_env\Scripts\activate

Cài thư viện:
pip install -r iot_canh_bao_demo/requirements.txt
```
#  2. Chạy CounterFit
python -m counterfit

Truy cập tại: http://localhost:5000

Cấu hình:

A0: Light Sensor

D2: Button (Cửa mở)

D4: LED (Cảnh báo)

# 3. Chạy Docker Compose
docker-compose up -d

Cổng mở:
Grafana: http://localhost:3000
InfluxDB: http://localhost:8086
MQTT (Mosquitto): localhost:1883

# 4. Chạy Telegraf
cd telegraf
telegraf.exe --config telegraf.conf

# 5. Chạy main.py
cd iot_canh_bao_demo
python main.py

-> Mỗi khi nhấn nút (mô phỏng mở cửa), hệ thống sẽ:
Gửi cảnh báo
Bật đèn LED
Gửi dữ liệu qua MQTT topic iot/canhbao

# 6. Xem dữ liệu trên Grafana
1. Truy cập http://localhost:3000
2. Đăng nhập: admin / admin
3. Tạo Data Source:
    - Type: InfluxDB
    - URL: http://localhost:8086
    - Database: telegraf
4. Tạo Dashboard:
    - Query: FROM mqtt_consumer
    - Fields: light, door_open
    - Chọn kiểu biểu đồ: Time series, Gauge...

# Test nhanh MQTT
mosquitto_pub -h localhost -t iot/canhbao -m "{\"light\": 100, \"door_open\": true}"
# Ghi chú
MQTT topic: iot/canhbao
Dữ liệu gửi dạng JSON

Hệ thống demo và có thể chưa hoàn thiện :33