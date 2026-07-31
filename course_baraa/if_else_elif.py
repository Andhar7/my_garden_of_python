

score = 72
is_project = False

if score >= 90 and is_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    if is_project:
        print("B+")
    else:
        print("B")
elif score >= 70 or is_project:
    print("C")
else:
    print("F")
    
number = 55
result_number = "A" if number >= 72 else "B"
print(result_number) # Only simple logic

number_second = 51
result_number = "A" if number_second >= 72 else "B" if number_second >= 55 else "Finish"
print(result_number) # Only simple logic



