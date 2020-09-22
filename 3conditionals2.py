def string_length(str):
    if(type(str)==int):
        print("Sorry integers don't have length")
    elif(type(str)==float):
        print("Sorry floats don't have length")
    else:
        print("The length of the string is ",len(str))

string_length(10);
string_length("simul")
string_length(6.47);
