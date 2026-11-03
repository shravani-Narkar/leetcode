class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        resulting_array = []
        concat_of_digits = ""

        for i in digits:
            concat_of_digits += str(i)
        back_to_int = int(concat_of_digits)
        output = back_to_int + 1
        str_output = str(output)
        for i in str_output:
            resulting_array.append(int(i))
        return resulting_array