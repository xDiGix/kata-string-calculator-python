class StringCalc():

    def add(self, numbers : str) -> int:
        result = 0
        if numbers == "":
            return result
        
        # split string with comma separetor
        nums = numbers.split(",")
        nums_int = [int(i) for i in nums]

        result = sum(nums_int)

        return result