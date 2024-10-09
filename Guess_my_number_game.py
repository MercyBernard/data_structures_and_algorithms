def get_positive_n():
    while True:
        try:
            n = int(input("Enter n: "))

            if n > 0:
                return n
            else:
                print("Enter a positive integer for n.")
        except:
            print("Enter a valid integer for n.")

n = get_positive_n()

print("Welcome to Guess My Number!")
print(f"Please think of a number between 0 and {n - 1}.")

low = 0
high = n - 1

while low <= high:
        guess = low + ((high - low)//2)

        print(f"Is your number {guess}?")
        print("Please enter C for correct, H for too high, or L for too low.")

        response = input("Enter your response (H/L/C): ").upper()

        while response not in ("C", "H", "L"):
            print("Please enter H, L, or C.")
            response = input("Enter your response (H/L/C): ").upper()

        if response == "C":
                print("Thank you for playing Guess My Number!")
                break

        elif response == "H":
                high = guess - 1

        elif response == "L":
                low = guess + 1

