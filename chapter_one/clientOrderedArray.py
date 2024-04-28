from OrderedArray import OrderedArray

max_size = 10

students_age = OrderedArray(max_size)

print(f"The number of students age recorded is {len(students_age)} with a capacity size of: {students_age.capacity()}")

students_age.insert(10)
students_age.insert(15)
students_age.insert(24)
students_age.insert(23)
students_age.insert(7)
students_age.insert(18)

print(f"The number of students age recorded is {len(students_age)} with a capacity size of: {students_age.capacity()}")

students_age.show()

print(students_age)

print(f"search for age 15: {students_age.search(15)}")
print(f"search for age 100: {students_age.search(100)}")

print(f"remove age 10: {students_age.delete(10)}")
print(students_age)
print(f"delete age 100: {students_age.delete(100)}")
print(f"get the age at index 20: {students_age.get(20)}")

