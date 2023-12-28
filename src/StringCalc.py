class StringCalc():

    delimiters: str = ","

    def add(self, numbers : str) -> int:
        result = 0
        if numbers == "":
            return result
        
        numbers = self.handle_format_delimiter(numbers)

        delimiter = self.delimiters

        # split string with two separetors
        numbers = numbers.replace("\n", delimiter)
        nums = numbers.split(delimiter)

        # cast string to int and remove numbers greater than 1000
        nums_int = [int(i) for i in nums if int(i) <= 1000]

        self.validate_numbers(nums_int)

        result = sum(nums_int)

        return result
    
    def handle_format_delimiter(self, numbers: str) -> str:
        # check if string starts with "//"
        if not numbers.startswith("//") or len(numbers) < 3:
            return numbers
        
        # remove "//"
        numbers = numbers[2:]
        string_splitted = numbers.split("\n")

        delimiter = string_splitted[0]
        self.delimiters = delimiter.replace("[", "").replace("]", "")

        numbers = string_splitted[1]

        return numbers
    
    def validate_numbers(self, numbers: list[int]) -> None:
        negative_number = [str(i) for i in numbers if i < 0]
        
        if len(negative_number) > 0:
            raise Exception("Negatives not allowed: " + ', '.join(negative_number))