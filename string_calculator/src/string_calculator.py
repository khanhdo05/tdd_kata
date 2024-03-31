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
        
        # Initiate an empty list to store negatives
        negatives = []
        
        # Iterate through the list, skip over empty string, convert str -> int, and add up to the sum
        for char in list_of_char:
            if char:
                num = int(char)
                
                if num < 0:
                    negatives.append(num)
                
                result += num
                
        if len(negatives) == 1:
            raise ValueError(f"negative: {negatives[0]} not allowed")
        elif negatives:
            raise ValueError(f"negatives: {', '.join([str(num) for num in negatives])} not allowed")
        
        return result