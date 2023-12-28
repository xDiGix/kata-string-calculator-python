class StringCalc():

    def add(self, numbers : str) -> int:
        result = 0
        if numbers == "":
            return result
        
        delimiter = ","
        # check if string starts with "//"
        if numbers.startswith("//") and len(numbers) >= 3:
            delimiter = numbers[2:3]
            numbers = numbers[4:]

        # split string with two separetors
        numbers = numbers.replace("\n", delimiter)
        nums = numbers.split(delimiter)
        nums_int = [int(i) for i in nums if int(i) <= 1000]

        negative_number = [str(i) for i in nums_int if i < 0]
        
        if len(negative_number) > 0:
            raise Exception("Negatives not allowed: " + ', '.join(negative_number))

        result = sum(nums_int)

        return result