marks = int(input("enter the marks obtained by the students :"))

if marks>= 90:
    print(f"student obtained {marks}. his perfomance is excellent")

elif marks>=80 and marks <90:
    print(f"student obtained {marks}. his perfomance is very good ")

elif marks>=70 and marks <80:
    print(f"student obtained {marks}. his perfomance is good  ")

elif marks>=60 and marks <70:
    print(f"student obtained {marks}. his perfomance is average  ")
    
else:
    print(f"student obtained {marks}. his perfomance is poor  ")
