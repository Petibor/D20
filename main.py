import random


def main():
    while True:
        print("Please enter a dice number or type exit to end program. 4-6-8-12-20")
        input1 = input();

        if input1 == "4" or input1 == "6" or input1 == "8" or input1 == "12" or input1 == "20":
            rolldice(input1)
        elif input1 == "exit":
            break
        else:
            print("Please enter a valid dice")


def rolldice(input):
    min = 1
    max = int(input);
    dice = random.randint(min, max)

    print("Your dice is " + str(dice) + "  Dice Type : D" + input);

    if dice > (int(input) / 100 * 70):
        print("Wow. A good one! That enemy has no luck ")


if __name__ == '__main__':
    main()
