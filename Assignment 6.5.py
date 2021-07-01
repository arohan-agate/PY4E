text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
numFinal = float(text[pos:len(text)])
print(numFinal)

print("testing, testing")