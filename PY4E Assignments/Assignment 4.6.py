def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return (h * r) + ((r * 0.5) * (h - 40))


inHrs = input("Enter Hours: ")
inRate = input("Enter Rate: ")
hrs = int(inHrs)
rate = float(inRate)

p = computepay(hrs, rate)

print("Pay", p)