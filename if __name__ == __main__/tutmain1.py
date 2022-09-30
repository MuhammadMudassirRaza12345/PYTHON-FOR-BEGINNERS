from ast import main


def printhar(string):
    return f"Harry is {string}"

def add(num1, num2):
    return num1 + num2 + 5

# ab ya yhi pr execute hoga

print("and the name is", __name__)
# O:and the name is __main__ #ya output main  aayega is waqt jab  ap is code ko yhi pr run kraga 
# ab ya yhi pr execute hoga
if __name__ == "__main__":
    print(printhar("Great"))
    o = add(4, 6)
    print(o)
     

 