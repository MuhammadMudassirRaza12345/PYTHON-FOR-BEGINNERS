# class Patient():
#     def __init__(self,name,gender,disease,contact):
#         self.Patient_name=name
#         self.Patient_gender=gender
#         self.Patient_disease=disease
#         self.Patient_contact=contact

#     def take_medicine(self):
#         print(f"{self.patient_name} is taking medicine")

#     def patient_details(self):
#         print(f"""
#         Name:{self.Patient_name}
#         Gender:{self.Patient_gender}
#         Disease: {self.patient_disease}
#         Contact: {self.patient_contact}

#        """)

#     # Getter
#     def get_name(self):
#         return self.Patient_name


#     # Setter
#     def set_name(self,newName):
#         self.patient_name = newName

#     def get_gender(self):
#         return self.patient_gender

#     # Setter
#     def set_gender(self,newGender):
#         self.patient_gender = newGender


# patient1 = Patient("Tom", "Male", "High Bp","12345678")
# patient1.Patient_name
# first argument is position argument, second argument is keyword argument
# cleanest_cities = ["karachi", "lahore", "islamabad","peshawar", "quetta"]
# flag=True
# while  flag==True:
#     user_input = input("Enter a city, or q toquit:")
#     if user_input != "q":
#         for a_clean_city in cleanest_cities:
#             if user_input == a_clean_city:
#                 print("It's one of the cleanest cities")
#                 break
#             else:
#                 print("It's not one of the cleanest cities")
#                 break

#     else:

#         flag=False


# def is_power_of_two(n):
#     while n % 2 == 0:
#         n = n / 2
#         if n == 1:
#             return True
#     return False

# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

n = 0
while n % 2 == 0:
    n = n / 2
    if n == 1:
        print(True)
