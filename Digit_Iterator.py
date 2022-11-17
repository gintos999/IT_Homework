def split_digits(number, base=10):
    if not (isinstance(number, int) and isinstance(base, int)):
        raise TypeError('All values must have int type')
    string = ''
    ans = ''
    while number > 0:
        if number % base > 10:
            string = string + chr(ord("A") + (number % base) % 10)
        else:
            string = string + str(number % base)
        number = number // base
    string = list(reversed(string))
    for j in range(len(string)):
        ans += string[j]
    return ans




for d in split_digits(number=123):
    print(d)


for d in split_digits(number=123, base=2):  # 123 (base 10) = 1111011 (base 2)
    print(d)
