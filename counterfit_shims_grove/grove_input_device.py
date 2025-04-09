from counterfit_connection import CounterFitConnection

class GroveInputDevice:
    def __init__(self, pin):
        self.pin = pin
        CounterFitConnection.init('127.0.0.1', 5000)  # Kết nối CounterFit
    
    def is_pressed(self):
        """Kiểm tra trạng thái nút nhấn (dùng cho cảm biến cửa)"""
        try:
            # Đọc giá trị digital pin từ CounterFit (Button ở Pin 0)
            return CounterFitConnection.get_sensor_boolean_value(self.pin) == 1
        except Exception as e:
            print(f"[GroveInputDevice] Lỗi đọc cảm biến: {e}")
            return False