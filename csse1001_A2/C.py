def dec2base(n,b):
    if n==0:
        return
    elif n<b:
        return[n]
    else:
        return dec2base(int(n/b),b)+[n%b]
