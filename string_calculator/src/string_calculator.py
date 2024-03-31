class StringCalculator():
    def Add(string):
        result = 0
        
        # When receive empty string, sum is 0
        if len(string) == 0:
            return 0
        
        # Split the string into a list of characters by comma as the delimiter
        list_of_char = string.split(",")
        
        # Iterate through the list, convert char -> int, and add up to the sum
        for char in list_of_char:
            result += int(char)

        return result