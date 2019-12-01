def palindrome(x):
    if 0 < x < 10000:
        if 10<=x<100:
            if x//10==x%10:
                return "palindrome"
            else:
                return "non palindrome"
        elif 100<=x<1000:
            if x//1000==x%10 and x//100==((x-(x//100)*100)//10):
                return "palindrome"
            else:
                return "non palindrome"
        elif 1000<=x<10000:
            if x//1000==x%10 and (x//100)%10==((x-(x//100)*100)//10):
                return "palindrome"
            else:
                return "non palindrome"
    else:
        return 'invalid value'

print(palindrome(17))
print(palindrome(330))
print(palindrome(57750))

