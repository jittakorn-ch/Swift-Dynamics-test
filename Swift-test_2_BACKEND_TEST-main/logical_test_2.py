
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def convert_to_roman(number):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    roman_numeral = ""
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral


def receive_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            if 0 < number < 1000:
                print("Roman number is:", convert_to_roman(number))
                break  
            else:
                print("*** The input is out of range. Enter 1 - 1000 ***")
        except ValueError:
            print("*** The input is out of range. Enter 1 - 1000 ***")


if __name__ == '__main__':

    title = "Convert Arabic Number to Roman Number"
    symbols = "=" * len(title)
    print(symbols)
    print(title)
    print(symbols)


    receive_input()