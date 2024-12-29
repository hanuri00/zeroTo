from signal imkport signal, SIGTERM, SIGHUP, pause
form rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, sae_exit)

try:
    lcd.text("Hello !!", 1)
    lcd.text("Raspberry pi!", 2)

    pause()

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
