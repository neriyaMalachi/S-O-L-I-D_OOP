def get_bonus(role):
    if role == "teacher":
        return 500
    elif role == "manager":
        return 1000
    # כל תפקיד חדש דורש שינוי בקוד הזה
    return 0

def  bad_Function_O():
    print(get_bonus("teacher"))
    print(get_bonus("manager"))
