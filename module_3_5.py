def get_multiplied_digits(numbers):
    str_number = str(numbers)
    if str_number[0] != 0:
        first = int(str_number[0])
        if len(str_number) > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first
    else:
        return 0


result = get_multiplied_digits(40203)
print(result)
