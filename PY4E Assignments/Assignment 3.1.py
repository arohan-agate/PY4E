inHrs = input("Enter Hours: ")
inpRate = input("Enter Rate: ")
hrs = int(inHrs)
rate = float(inpRate)
if hrs <= 40:
    print(hrs*rate)
else:
    originalPay = 40 * rate
    newRate = rate * 1.5
    bonusPay = (hrs - 40) * newRate
    print(originalPay + bonusPay)