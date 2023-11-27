import random
import time

def print_out_animation(out):
    print(out[0])
    time.sleep(0.5)
    print(f"{out[0]}/{out[1]}")
    time.sleep(1)
    print("/".join([i for i in out]))

def choice():

    symbols = ["A", "B", "C"]
    out = []

    for _ in range(3):
        out.append(random.choice(symbols))
    return out

def calculate_Players_balance(balance, deposite, out1, out2, out3):
        won = True
        balance -= deposite
        if out1 == out2 and out2 == out3:
            deposite *=2
        else:
            deposite= 0
            won = False

        balance += deposite
        return balance, won

def print_animation(won, balance):
    if won:
        time.sleep(0.5)
        print("congratulations")
    print(f"your balance is: {balance}")



def main():

    balance = 100
    play = True

    while play:

        deposite = int(input("enter a deposite: "))

        if deposite > balance:
            print("not enough money")
            break

        #result and animation
        out = choice()
        print_out_animation(out)

        #balance
        balance, won = calculate_Players_balance(balance, deposite, out[0], out[1], out[2])
        print_animation(won, balance)

        y_n = input("wanna play again (y, n): ")

        if y_n == "y":
            continue
        else:
            play = False

main()