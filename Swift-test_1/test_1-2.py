"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python
เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 
โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""


# หา index ของค่าที่มากที่สุดใน array
def find_largest_index(numbers):
    max_index = 0  
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
    return max_index


# เช็คค่าใน array ว่าเป็นตัวเลขทั้งหมดหรือไม่
def check_numbers(numbers):
    for num in numbers:
        if not isinstance(num, (int, float)):   # check if not 'integer' or 'float' return Flase
            return False
    return True



if __name__ == "__main__":

    numbers = [1, 2, 1, 3, 5, 6, 4, -78]

    # เรียกใช้งาน
    if check_numbers(numbers):
        result = find_largest_index(numbers)
        print("The index of the largest number is:", result)
    else:
        print(numbers, 'มีค่าผิดปกติ')

