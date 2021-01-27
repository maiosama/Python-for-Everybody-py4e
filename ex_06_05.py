text = "X-DSPAM-Confidence:    0.8475";
x= text[text.find("0") : text.find("5")+1]
n=float(x)
print(n)
