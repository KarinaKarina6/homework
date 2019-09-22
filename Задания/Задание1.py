def parking(day,hour):
    if hour > 23 or hour < 0 or day < 1 or day > 31:
        return 'invalid value'
    elif 19 <= hour < 21:
        return 'both'
    elif day % 2 == 0:
        if 21 <= hour <= 23:
            return 'left'
        else:
            return 'right'
    else:
        if 21 <= hour <= 23:
            return 'right'
        else:
            return 'left'

print(parking(30,20))
print(parking(4,5))
print(parking(17,2))
print(parking(32,8))

