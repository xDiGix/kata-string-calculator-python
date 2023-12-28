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
        nums_int = [int(i) for i in nums]

        result = sum(nums_int)

        return result