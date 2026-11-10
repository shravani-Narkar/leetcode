class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        list_n = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                list_n.append("FizzBuzz")
            elif i % 3 == 0:
                list_n.append("Fizz")
            elif i % 5 == 0 :
                list_n.append("Buzz")
            else:
                list_n.append(str(i))
        return list_n