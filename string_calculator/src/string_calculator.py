class StringCalculator():
    def Add(string):
        result = 0
        
        # When receive empty string, sum is 0
        if len(string) == 0:
            return 0
        
        # Replace any non-digit character with a comma
        string_with_only_commas_as_delimiter = ''.join([char if char.isdigit() or char == "-" else "," for char in string])
        
        # Split the string into a list of characters by comma as the delimiter
        list_of_char = string_with_only_commas_as_delimiter.split(",")
        
        # Iterate through the list, skip over empty string, convert str -> int, and add up to the sum
        for char in list_of_char:
            if char:
                num = int(char)
                
                if num < 0:
                    raise ValueError(f"negatives: {num} not allowed")
                
                result += num

        return result