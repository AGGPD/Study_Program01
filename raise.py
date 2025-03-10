def no_negative(num):
    if num < 0:
        raise ValueError("I said no negative")
    return num

print(no_negative(-1))