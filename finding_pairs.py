def main():
    print(
        "Welcome! this program will tell you all the pairs of positive two digit numbers whose sum is 60."
    )


for num1 in range(10, 100):
    num2 = 10
    while num2 < 100:
        if num1 + num2 == 60 and num1 <= num2:
            print(f"({num1}, {num2})")
        num2 += 1

if __name__ == "__main__":
    main()
