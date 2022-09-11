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
#first argument is position argument, second argument is keyword argument

def add_numbers(first_number=2,second_number=4):
    total = first_number  + second_number
    print(total)   

add_numbers()    