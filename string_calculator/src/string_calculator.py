class StringCalculator():
    def Add(string):
        result = 0
        if len(string) == 0:
            return 0
        list_of_char = string.split(",")
        for char in list_of_char:
            result += int(char)
        return result