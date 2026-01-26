def int_to_roman(num):
    val = [
        (1000, "M"),  (500, "D"),
        (100, "C"),  (50, "L"),
        (10, "X"), (5, "V"), 
        (1, "I")
    ]
    
    roman = ""

    for (number, numeroman) in val:

        while num >=number:
            roman += numeroman
            num -=number

    return roman
num=int(input("Enter an integer number: "))
print(int_to_roman(num))