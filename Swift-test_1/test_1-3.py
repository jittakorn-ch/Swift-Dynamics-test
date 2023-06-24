"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 
10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""


# หาค่า fatorial 
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
    return result


# นับจำนวนเลข 0 ที่อยู่ท้ายของจำนวนเต็ม
def count_zero(num):
    num_str = str(num)
    count_zeros = 0
    for i in reversed(num_str):
        if i == '0':
            count_zeros += 1
        else:
            break
    return count_zeros


# หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
def find_zoro(num):
    if not isinstance(num, int) or num < 0:  # ไม่ใช่จำนวนเต็ม หรือ น้อยกว่า 0
       return ("The input is not a positive integer.")
    else:
        factorial_value = factorial(num)
        zero_num = count_zero(factorial_value)
        return f'Number of connected zeros at the end: {zero_num}'
    


if __name__ == "__main__":

    #เรียกใช้
    result = find_zoro(1)
    print(result)
