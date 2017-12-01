"""Functions to deal with representations of integers in various bases"""

def show_base(num, base):
    """Show an integer as its string representation in the given base"""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    try:
        result = ""
        while num > 0:
            result += digits[num % base]
            num = num // base
        result = "0" if result == "" else result
        return result[::-1]
    except IndexError:
        print("Base should be between 2 and 36.")

def read_base(string, base):
    """Read a string in the given base as an integer"""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    try:
        total = 0
        power = 1
        while string != "":
            total += digits.index(string[-1:]) * power
            power *= base
            string = string[:-1]
        return total
    except IndexError:
        print("Base should be between 2 and 36.")

def test():
    """Test the thing"""
    for base in range(2, 37):
        print("Base " + str(base) + ":")
        for i in range(20):
            print(show_base(i, base), end=" ")
            assert i == read_base(show_base(i, base), base)
        print()
