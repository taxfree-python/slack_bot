def fizzbuzz(text):
    text_s = text.split()
    text_1 = text_s[1]
    number = float(text_1)
    if number % 3 == 0 and number % 5 ==0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        number_int = int(number)
        return str(number_int)