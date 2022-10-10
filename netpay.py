emplyid=input("Employee ID: ")
emplyname=input("Employee Name: ")
basicpay=int(input("Basic Pay: "))
def high():
    hra=(0.15*basicpay)
    da=(0.08*basicpay)
    netpay=basicpay+(hra+da)
    print("HRA is: ",hra)
    print("DA is: ",da)
    print("Net Pay: ",netpay)
def medium():
    hra=(0.10*basicpay)
    da=(0.05*basicpay)
    netpay=basicpay+(hra+da)
    print("HRA is: ",hra)
    print("DA is: ",da)
    print("Net Pay: ",netpay)
def slow():
    hra=(0.05*basicpay)
    da=(0.03*basicpay)
    netpay=basicpay+(hra+da)
    print("HRA is: ",hra)
    print("DA is: ",da)
    print("Net Pay: ",netpay)
if basicpay>10000:
    high()
elif basicpay>=5000 and basicpay<=10000:
    medium()
elif basicpay<5000:
    slow()
    




