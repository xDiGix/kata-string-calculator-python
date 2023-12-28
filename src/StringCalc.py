import re

class StringCalc():

    delimiters: list[str] = []

    def add(self, numbers : str) -> int:
        result = 0
        if numbers == "":
            return result
        
        numbers = self.handle_format_delimiter(numbers)

        default_delimiter = ","

        # split string with two separetors
        numbers = numbers.replace("\n", default_delimiter)

        # replace delimiters with default
        for delimiter in self.delimiters:
            numbers = numbers.replace(delimiter, default_delimiter)

        nums = numbers.split(default_delimiter)

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
        # split format delimiter and numbers
        string_splitted = numbers.split("\n")

        delimiter = string_splitted[0]
        numbers = string_splitted[1]

        matches = re.findall(r'\[(.*?)\]', delimiter)
        if len(matches) > 0:
            delimiter = matches
        
        # force delimiter to be a list
        if not isinstance(delimiter, list):
            delimiter = [delimiter]

        self.delimiters = delimiter

        return numbers
    
    def validate_numbers(self, numbers: list[int]) -> None:
        negative_number = [str(i) for i in numbers if i < 0]
        
        if len(negative_number) > 0:
            raise Exception("Negatives not allowed: " + ', '.join(negative_number))