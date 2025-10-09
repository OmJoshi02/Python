try:
    num = 10
    res = 100 / num

except ZeroDivisionError:
    print("Error occurred")

else:
    print("Result : ",res)

finally:

    print("Program completed")