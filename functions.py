def addTwoNumbers(number1:float, number2:float) -> float:

    if type(number1) not in [float, int]:
        raise TypeError(f'{number1} must not be a number');
    if type(number2) not in [float, int]:
        raise TypeError(f'{number2} must not be a number');

    if number1 < 0:
        raise ValueError(f'{number1} must not be less than 0');
    if number2 < 0:
        raise ValueError(f'{number2} must not be less than 0');

    return number1 + number2


