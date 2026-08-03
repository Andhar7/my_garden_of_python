

# range(start, stop, step)
example_range = range(0, 12, 3)
for e in example_range:
    if e % 2 == 0:
        print(f"Even numbers: {e}")
    else:
        print(f"Range of start, stop and step: {e}")

example_range_even = range(0, 12, 2)
for e in example_range_even:
    print(f"Range of even numbers: {e}")
    
example_range_odd = range(1, 12, 2)
for e in example_range_odd:
    print(f"Range of odd numbers: {e}")
    
scores = [212, 323, 435, 12, 87]
total = 0
for score in scores:
    total += score
    print(f"Current total: {total}")
print(f"Final total : {total}")

files = [' Report.csv', 'DATA.csv ', ' FINAL.TXT ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing....: {file}")
    
result = 7
final = []
for number in range(1, 11):
    final = result * number
    print(f"Current {number} result: {final}")
print(f"Final result : {final}")

star = "*"
final = []
for number in range(1, 7):
    final = star * number
    print(f"Current {number} result: {final}")
print(f"Final result : {final}")

names = [ 'guru', 'kumar', 2, 'andrej', 'bob', '', 'tatjana']
for name in names:
    if name == '':
        print("Detected empty name!")
        break
    if name == 2:
        print(f"Ooops... here number which skiped and continue...")
        continue
    if name == 'andrej': 
        pass # TODO Handle empty value 
        name = name.replace('andrej', 'mahadev')
    print(f"All names is: {name.capitalize()}")
    
days = ["Mo", "Tu", "Wed", "Thous", "Fri", "Sut", "Sun"]
for day in days: 
    if day == days[-1]:
        continue
    if day == days[-2]:
        continue
    print(f"Here all working days: {day}")

days = ["Mo", "Tu", "Wed", "Thous", "Fri", "Sut", "Sun"]
for day in days: 
    if day in days[-2:]:
        continue
    print(f"Here all working days: {day}")

days = ["Mo", "Tu", "Wed", "Thous", "Fri", "Sut", "Sun"]
weekends = ["Sut", "Sun"]
for day in days: 
    if day in weekends:
        continue
    print(f"Here all working days: {day}")
    

emails = [
    'andrej@gmail.com',
    'bara@express.io',
    'DROP TABLE USERS;',
    'xvid@gmail.com',
]
for email in emails:
    if ';' in email:
        print("SQL Injection: Hackers Attack")
        break

even_check = [1, 3, 4, 7, 12]
for even in even_check:
    if even % 2 == 0:
        print(f"Here even numbers: {even}")
        break
else:
    print("All numbers are odd!")
    

names = ['Kamara', 'Andrej', 'Tatjana', None, 'Kumar']
for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available!")

files = [
    'data.csv',
    'merge.pdf',
    'follow.txt',
    'beyound.csv',
]
for file in files:
    if not file.endswith('csv'):
        print(f"We found files which not include .csv : {file}")
        continue 

for file in files:
    if not file.endswith('csv'):
        print("Not all files with .csv")
        break
else:
    print("All files in csv")
    
print("===  ===")
# Challenge
file_list = [
    'report.csv',
    'merge.xlsx',
    'merge.xlsx',
    'merge.xlsx',
    'follow.docs',
    'follow.docs',
    'beyound.csv',
    'report.csv'
]
  # Solution 2
print("=== Solution 2 ===")

seen = set()
for file in file_list:
    if file_list.count(file) > 1 and file not in seen:
        print(f"Duplicate files here: {file}")
        seen.add(file)
        
# Professional way using counter
  # Solution 3
print("\n=== Solution 3 (Professional) ===")

from collections import Counter
counts = Counter(file_list)

for file, count in counts.items():
    if count > 1:
        print(f"Duplicate {file} appears {count} times...")


print("\n=== Solution (Professional Way) ===")
# Challenge. Find the file that appeared most
most_common_file, most_common_count = counts.most_common(1)[0]
print(f"Most duplicated files: {most_common_file} {most_common_count} times")

# Challenge: Find all files appearing more then 2 times
print("\n Files appearing more then 2 times...")
for file, count in counts.items():
    if count > 2:
        print(f"File : {file} count : {count} times")



        
        

