def solution(x, y):
    count = 0
    x = int(x)
    y = int(y)

    while x != 1 or y != 1:
        if x == 1 or y == 1:
            if x == 1:
                count += y - 1
            if y == 1:
                count += x - 1
            break

        if x < y:
            if x == 0:
                return "impossible"
            count += y / x
            y %= x
        else:
            if y == 0:
                return "impossible"
            count += x / y
            x %= y

    return str(count)

