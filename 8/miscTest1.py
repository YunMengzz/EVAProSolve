import base64
flag='RVZBe1czMWMwbUVfVG9fekp1RVY0X1QzY2hAPz8/Pz99Ck1ENTo5NDY4NkM1N0U1MTIzNDkyOEIzNDQ5MjRGOTkyRDlDOQ=='
base32='abcdefghijkmnlopqrstuvwxyz0189+/'
base16='GHIJKMNLOPQRSTUVWXYZabcdefghijkmnlopqrstvuwxyz+/'
def check(flag):                
    for i in base16:
        if i in flag:
            for b in base32:
                if b in flag:
                    return 64
                    exit(0)
                return 32
                break
        return 16
        exit(0)
for i in range(20):               
    num=check(flag)
    if num==16:
        print('16：'+flag)
        try:
            flag=base64.b16decode(flag)
        except:
            flag=base64.b64decode(flag)
        flag=flag.decode()
    elif num==32:
        print('32：'+flag)
        try:
            flag=base64.b32decode(flag)
        except:
            flag=base64.b64decode(flag)
        flag=flag.decode()
    else:
        print('64：'+flag)
        flag=base64.b64decode(flag)
        flag=flag.decode()
print(flag)
