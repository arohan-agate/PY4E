largest = None
smallest = None
while True:
    n = input("Enter a number: ")

    if n == "done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break

    try:
        num = int(n)
        if largest is None:
            largest = num
        elif num > largest:
            largest = num

        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
    except:
        print("Invalid input")
        continue