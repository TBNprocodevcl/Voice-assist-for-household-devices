import RPi.GPIO as GPIO
import time

# Thiết lập chế độ chân GPIO
GPIO.setmode(GPIO.BOARD)

# Chân GPIO được sử dụng để kết nối với relay
relay_pin = 11

# Thiết lập chân GPIO là đầu ra
GPIO.setup(relay_pin, GPIO.OUT)

# Hàm để bật đèn
def turn_on():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Đèn đã được bật.")

# Hàm để tắt đèn
def turn_off():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Đèn đã được tắt.")

# Chạy chương trình
try:
    while True:
        turn_on()
        time.sleep(5)
        turn_off()
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
