def collatz(number):
    # PEP 285 "Strong and bitter words indicate a weak cause."
    if number % 2:
        number = 3 * number + 1
    else:
        number = number // 2
        
    print(number)
    return number

def main():
    innie = input("Enter number: ")
    
    try:
        innie = int(innie)
        
        # Handle error causing infinite loop
        if innie <= 0:
            raise ValueError

        while innie != 1:
            innie = collatz(innie)
        
    except ValueError:
        # Took liberty to include specifying greater than zero
        print("You must enter an integer greater than zero.")
        main()

if __name__ == "__main__":
    main()
