"""This code takes a user input in degrees Fahrenheit and converts it into
degrees Celcius
"""


def main():
    print('Please enter a number in degrees Fahrenheit')
    user_input = input()

    try:
        val = float(user_input)
        result = f_to_c(val)
        print(f'{user_input} degrees F is equal to {result} degrees C')
    except ValueError:
        print('Please enter a valid number.')


def f_to_c(x):
    """Converts a number from degrees F to degrees C"""
    y = (x - 32) * 5 / 9
    return y


if __name__ == '__main__':
    main()
