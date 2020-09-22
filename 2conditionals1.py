def celsiustofahrenheit(cel):
    if(cel<-273.15):
        print("The lowest possible temperature that physical matter can reach is -273.15C. Invalid input")
    else:
        far = cel * 9/5 +32
        print("The fahrenheit equivalent is ", far)


celsiustofahrenheit(10);
celsiustofahrenheit(-274);
