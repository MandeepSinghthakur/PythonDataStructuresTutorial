import math

PI = math.pi

def area(radius):
    global z
    z = 6 
    theArea = PI * radius **2
    return theArea

def main():
    global z
    historyofPrompts = []
    historyofOutputs = []
    def getInput(prompt):
        x = input(prompt)
        historyofPrompts.append(prompt)

        return x
    
    def showOutput(val):
        historyofOutputs.append(val)
        print(val)
    
    rString = getInput("PLease Enter the radius of the circle: ")

    r  = float(rString)

    val = area(r)
    print(z)
    showOutput("The Area of the Circle is " + str(val))

if __name__ == "__main__":
    main()