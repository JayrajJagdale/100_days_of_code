def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("jAYrAj","jaGdALE"))
# output = format_name("jAyrAj","jAgDalE")
# print(output)

def formated_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide correct input"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(formated_name(input("Enter F Name: "),input("Enter L Name: ")))