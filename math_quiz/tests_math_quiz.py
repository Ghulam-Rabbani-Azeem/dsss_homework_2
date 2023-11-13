import unittest
from math_quiz import random_num, sign_choose, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_num(self):
        # Test if random numbers generated are within the specified range
        min_num = 1
        max_num = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_num, max_num)
            self.assertTrue(min_num <= rand_num <= max_num) #Asserts true if the conditions are true
        min_num = 10
        max_num = 100
        for _ in range(200):  # Test a large number of random values
            rand_num = random_num(min_num, max_num)
            self.assertTrue(min_num <= rand_num <= max_num)
        min_num = 100
        max_num = 1000
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_num, max_num)
            self.assertTrue(min_num <= rand_num <= max_num)
        min_num = 1000
        max_num = 10000
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_num, max_num)
            self.assertTrue(min_num <= rand_num <= max_num)


    def test_sign_choose(self):
        # Test is the choice exist in already defined function
        for _ in range (200):
            operator = sign_choose()
            self.assertTrue(operator=="+" or "-" or "*")
        for _ in range (200):
            operator = sign_choose()
            self.assertTrue(operator=="-" or "+" or "*")
        for _ in range (200):
            operator = sign_choose()
            self.assertTrue(operator=="*" or "-" or "+")
 
        

    def test_math_operation(self):
            test_cases = [
                (30, 5, '+', '30 + 5', 35),
                (15, 5, '-', '15 - 5', 10),
                (2, 2, '*', '2 * 2', 4),
                (22, 2, '-', '22 - 2', 20),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                solution= math_operation(num1,num2,operator)
                
                self.assertTrue(solution[0]==expected_problem)
                self.assertTrue(solution[1]==expected_answer)



if __name__ == "__main__":
    unittest.main()
