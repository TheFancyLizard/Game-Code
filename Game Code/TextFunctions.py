import time


# Write (...) slowly
def wait_time():
    for i in range(3):
        print(".", end="")
        time.sleep(1)
    time.sleep(1)
    print("\n")


# Write message character per character
def write_slow(message):
    for i in message:
        print(i, end="")
        time.sleep(0.2)


#write message and pause
def write_n_wait(message):
    print(message)
    time.sleep(2)


def player_speech(message):
    print(f"\033[1;90;107m{message}\033[1;0;0m")
    time.sleep(2)


def merchant_speech(message):
    print(f"\033[1;92m{message}\033[1;0;0m")
    time.sleep(1)


def red_message(message):
    print(f"\033[1;30;101m{message}\033[1;0;0m")
    time.sleep(2)


def green_message(message):
    print(f"\033[1;30;102m{message}\033[1;0;0m")
    time.sleep(2)


def pink_message(message):
    print(f"\033[1;30;105m{message}\033[1;0;0m")
    time.sleep(2)


def yellow_message(message):
    print(f"\033[1;30;103m{message}\033[1;0;0m")
    time.sleep(2)
