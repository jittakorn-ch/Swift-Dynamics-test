
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

THAI_TEXT_NUMBERS = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
UNITS = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")


def number_to_thai_text(number):
    digit_list = [int(digit) for digit in str(number)]  # แยกตัวเลขเข้า list  # Ex. 345 -> [3, 4, 5]

    result = ""
    thai_text = ""
    for i, digit in enumerate(digit_list):       #(index, value) # enumerate วนลูปรับค่า index และ value ได้  
        unit_index = len(digit_list) - i - 1    # ค่า index 
        unit = UNITS[unit_index]                # map ค่า index กับ UNITS
        if digit == 0:
            thai_text = ""
        elif digit == 1 and unit_index == 1:
            result += unit
        elif digit == 0 and unit_index == 0:
            break
        else:      
            if digit == 2 and unit_index == 1:
                thai_text = "ยี่"
            elif digit == 1 and unit_index == 0:
                thai_text = "เอ็ด"
            else:
                thai_text = THAI_TEXT_NUMBERS[digit]    # map ค่าด้วย value
            result += (thai_text + unit)

    return result


# receive and check input
def receive_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            if 0 <= number < 10_000_000:
                print(number_to_thai_text(number))
                break  
            else:
                print("***The input is out of range. try agian***")
        except ValueError:
            print("***The input is out of range. try agian***")



if __name__ == '__main__':

    title = "Convert Number to Thai Text"
    symbols = "=" * len(title)
    print(symbols)
    print(title)
    print(symbols)


    receive_input()

