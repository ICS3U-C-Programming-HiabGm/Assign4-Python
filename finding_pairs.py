# Created by: Hiab G
# Date: Wed, May. 3rd
# This program gets

def printing_pairs():
    # Print all valid pairs whose sum is 60
    print("\nAll pairs of two-digit numbers whose sum is 60:")
    for num1 in range(10, 100):
        for num2 in range(num1, 100):
            if num1 + num2 == 60:
                print(f"({num1}, {num2})")


def main():
    #welcome message 
    print("Welcome! This program will tell you all the pairs of positive two-digit numbers whose sum is 60.")

    #Ask user for input and catch errors
    try:
        user_input = int(input("Enter a two-digit number: "))

#
    
    except Exception:
        print("Please enter a valid input.")
    



if __name__ == "__main__":
    main()
