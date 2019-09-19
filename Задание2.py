def palindrome(n):
    if 0<n<1000:
        p = list(str(n))
        if len(str(n)) % 2 != 0:
            p.insert(0, '0')
        if p == p[::-1]:
            print("palindrome")
        else:
            print("non palindrome")
    else:
        print('invalid value')

