
def convert_c_to_f(temp_in_celsius):
    temp_in_fareheight = temp_in_celsius*1.8 + 32
    return temp_in_fareheight
temprature_in_f = convert_c_to_f(20)
print(temprature_in_f)
