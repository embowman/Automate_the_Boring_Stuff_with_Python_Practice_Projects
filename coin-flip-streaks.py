import random

# modified to calculate for input streak length

def flipCoin():
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        if experimentNumber == 626:
            print("Ohana means family.")
            
        # create a list of 100 'heads' or 'tails' values
        flips = []
        for i in range(100):
            flips.append(random.randint(0, 1))
            
        # check if there is a streak
        s = 0
        for i in range(1, 100):
            if flips[i] == flips[i - 1]:
                s += 1
            else:
                if s == 6:
                    numberOfStreaks += 1
                s = 0
    return numberOfStreaks

def main():
    streaksNum = flipCoin()
    print("Number of streaks with six flips: " + str(streaksNum))
    print("Percentage of all flips included in those streaks: ", end="")
    print(str((streaksNum * 6) / 10000) + "%")

if __name__ == "__main__":
    main()

# deviated from challenge's provided output template        
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
