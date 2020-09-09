def encode(k):
        if k // 2 != 0:
                encode(k // 2)
        csl = k % 2
        print(csl, sep="", end="")

def decode(k): 
        leng = len(str(k))
        kstr = ''.join(reversed(str(k)))
        answ = 0 
        for x in range(0, leng):
                if (kstr!="0"):
                        answ = (int(kstr[x])*(2**x))+answ
        print(answ)

# write encode to convert decimal number at binary number
# write decode to conver binary number at decimal number
# syntax encode(<your number>) decode(<your number>)
