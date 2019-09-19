def parking(day,hour):
    if hour >= 24.00 or hour < 0.00 or day < 1 or day > 31:
        return 'invalid value'
    elif 19.00 <= hour < 21.00:
        return 'both'
    elif day % 2 == 0:
        if 21.00 <= hour <= 23.59:
            return 'left'
        else:
            return 'right'
    else:
        if 21.00 <= hour <= 23.59:
            return 'right'
        else:
            return 'left'

