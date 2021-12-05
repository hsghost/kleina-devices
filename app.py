#!/usr/bin/env python3

from asyncio import sleep
import asyncio as aio

from periphery import GPIO, LED, PWM, SPI, I2C, MMIO, Serial

# TODO: Environment Variables: DEV_GPIO, DEV_PWM, DEV_SPI, DEV_I2C, DEV_UART, etc...
PIN_GPIO_OUT = [17, ]
PIN_GPIO_IN = [1, ]
PIN_PWM = [[32], [33], [42], ]
PIN_UART = [("/dev/ttyS1", 8, 10, 18, 16), ("/dev/ttyS2", 32, 33, ), ("/dev/ttyS3", 37, 36, ), ("/dev/ttyS4", 13, 15, 29, 11)] # (devpath, TX, RX, RTSN, CTSN)

# Setting up device pins
gpio_out_pins = []
for pin in PIN_GPIO_OUT:
    gpio_out_pins[pin] = GPIO(pin, "out")
gpio_in_pins = []
for pin in PIN_GPIO_IN:
    gpio_in_pins[pin] = GPIO(pin, "in")
pwm_pins = []
for chip in PIN_PWM:
    for pin in chip:
        pwm_pins[pin] = PWM(PIN_PWM.index(chip), pin)

# Setting up UART
uarts = []
for uart in PIN_UART:
    if len(uart) == 4:
        uarts[PIN_UART.index(uart)] = Serial(uart[0], 115200, rtscts = True)
    elif len(uart) == 2:
        uarts[PIN_UART.index(uart)] = Serial(uart[0], 115200)

def set_gpio_out_pin(gpiopin, level) -> None:
    gpiopin.write(level)

def get_gpio_in_pin(gpiopin) -> int | bool:
    return gpiopin.read()

def set_pwm_pin(pwmpin, duty_cycle, freq) -> None:
    if freq:
        pwmpin.frequency(freq)
    pwmpin.duty_cycle = duty_cycle

def start_pwm(pwmpin) -> None:
    pwmpin.enable()

def read_uart(length, timeout) -> str:
    pass

def write_uart(data) -> None:
    pass

def pin_lock_rising():
    pass

async def unlock_doors() -> int:
    pass

async def light_up() -> int:
    pass

async def light_down() -> int:
    pass

async def check_lock_status() -> bool:
    pass

async def enable_rfid(rfid_en_pin: int) -> int:
    pass

async def handel_signal(reader, writer):
    data = await reader.read()
    signal = data.decode()
    if signal == "":
        pass
    elif signal == "":
        pass
    else:
        pass

async def app():
    async with await aio.start_server(handel_signal, port=32123) as server:
        await server.serve_forever()

if __name__ == '__main__':
    aio.run(app())
