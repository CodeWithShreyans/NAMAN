from machine import Pin, ADC
from utime import sleep

# CO
s7 = Pin(22, Pin.IN)

# Methane
s5 = ADC(Pin(26, Pin.IN))

# H2S
s136 = ADC(Pin(27, Pin.IN))

# NH3, CO2
s135 = ADC(Pin(28, Pin.IN))

red = Pin(10, Pin.OUT)
yellow = Pin(11, Pin.OUT)
green = Pin(12, Pin.OUT)

buzzer = Pin(15, Pin.OUT)

green.high()
yellow.low()
red.low()
buzzer.low()


while True:
    print("\n\n")
    s5r = s5.read_u16()
    s7r = s7.value()
    s135r = s135.read_u16()
    s136r = s136.read_u16()

    print("s5: ", s5r)
    print("s7: ", s7r)
    print("s135: ", s135r)
    print("s136: ", s136r)

    if s5r < 12500 and s135r < 12500 and s136r < 12500:
        green.high()
        yellow.low()
        red.low()
        buzzer.low()
    elif s5r < 15000 and s135r < 15000 and s136r < 15000:
        green.low()
        red.low()
        yellow.high()
        buzzer.low()
    else:
        green.low()
        red.high()
        yellow.low()
        buzzer.high()

    sleep(0.5)
    red.low()
    sleep(0.5)
