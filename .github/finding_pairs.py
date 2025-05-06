# Created by: Hiab G
# Date: Wed, May. 3rd
# This program gets all pairs of two-digit numbers whose sum is 60


def printing_pairs():
    # Print all valid pairs whose sum is 60
    print(
        "\nAll pairs of two-digit numbers whose sum is 60 (using for and while loop):"
    )

    counter_num1 = 0  # Counter for outer loop

    # Using for loop for num1
    for num1 in range(10, 61):
        counter_num1 += 1
        num2 = num1
        counter_num2 = 0  # Counter for inner loop

        # Using while loop for num2
        while num2 < 100:
            if num1 + num2 == 60:
                print(f"({num1}, {num2})")
            num2 += 1
            counter_num2 += 1


def main():
    # Welcome message
    print(
        "Welcome! This program will tell you all "
        "the pairs of positive two-digit numbers whose sum is 60."
    )

    # Ask user for input and catch errors
    try:
        user_input = int(input("Enter a two-digit number: "))  # Conversion on one line

        # Check if the input is a valid two-digit number between 10–59
        if 10 <= user_input <= 59:
            pair2 = 60 - user_input
            if 10 <= pair2 <= 59:
                print(f"The number that adds up to 60 with {user_input} is {pair2}.")
            else:
                print(f"No valid two-digit number adds up to 60 with {user_input}.")
        else:
            print("Invalid Input. Please enter a two-digit number between 10 and 59.")

    except Exception:
        print("Invalid input! Please enter a valid two-digit integer.")

    # Call function
    printing_pairs()


if __name__ == "__main__":
    main()
