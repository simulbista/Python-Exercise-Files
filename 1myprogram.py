def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Exceptiom: Cannot divide by 0"

print("Hello")
print(divide(5,2))
print(divide(1,0))
