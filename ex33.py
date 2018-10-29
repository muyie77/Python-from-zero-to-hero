def number():
    i = 0
    increment = int(input("Enter the number of increment you want: "))
    n = int(input("Enter a number: "))
    numbers = []

    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The number is: ")

    for num in numbers:
        print(num)
