from Array import Array

def jet():
    print("===========================================================================================================")


array_size = 5

student_record = Array(array_size)

print(f"The number of names in the student record is {len(student_record)}")

jet()

student_record.insert("Mary")
student_record.insert("James")
student_record.insert("Paul")
student_record.insert("Grace")
student_record.insert("Ruth")


print(f"The number of names in the student record is {len(student_record)}")
student_record.show()
jet()

student_record.set(0, "Linda")
print(f"{student_record.get(0)} is now recorded in the student record")

jet()
print("is Paul present?.....say your name louder....", student_record.search("Paul"))

jet()
print("Ruth stop schooling, so delet her name", student_record.remove("Ruth"))
student_record.show()
print("is Eric removed from the record", student_record.remove("Eric"))

jet()

print("find me Eric", student_record.search("Eric"))
