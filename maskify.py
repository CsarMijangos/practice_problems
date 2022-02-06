def maskify(cc):
    R = ""
    l = len(cc)
    if l<5:
        print(cc)
        return cc
    else:
        for i in range(0,l-4):
            R= "#"+ R
        R = R + cc[l-4:]
        print(str(R))
        return R
maskify("solteco")
maskify("solo")
maskify("dos")
maskify("")
maskify("      ")
