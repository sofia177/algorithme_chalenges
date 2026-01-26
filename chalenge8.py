def int_to_roman(num):
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    roman = ""
    for (number, numeroman) in val:
        while num >=number:
            roman = roman+ numeroman
            num = num - number
    return roman
num=int(input("Enter an integer number: "))
print(int_to_roman(num))