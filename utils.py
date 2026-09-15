class utils:
    def __init__(self):
        pass

    def reversed(self, number):
        number_reversed = int(str(number)[::-1])
        return number_reversed
    
    def formatter(self, number):
        number_octal = oct(number)
        return number_octal
