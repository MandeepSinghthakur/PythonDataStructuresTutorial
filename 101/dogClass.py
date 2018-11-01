print("Start")
import time
tick = time.clock()
print(tick)
class Dog:
    # this is the constructor for the class. It is called whenever a Dog
    # Object is created. The reference "self" is created by Python and 
    # made to point to the space for the newly created Object
    # Python does this automatically for us but we have "self" as the first
    # parameter to the _init__ method (i:e the constructor)

    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

        #This is an accessor method that returns the speakText stored in the
        #Object. Notice that "self" is a parameter. Every method has "self" as its
        #first parameter. The "self" parameter is a reference to the current
        # Object. The current object appears on the left hand side of the dot (i.e the .)
        # when mehtod is called

    def speak(self):
            return self.speakText

        #Here is the accessor method to get the name
    def getName(self):
            return self.name

        
        #This is another accessor method that uses the birthday information to 
        #return a string representing the date.
    def birthDate(self):
            return str(self.month) + "/" + str(self.day) + "/" + str(self.year)


        #This is a mutator mehthod that changes the speackText of the Dog Object.
    def changeBark(self,bark):
            self.speakText = bark

        
        # When Creating the new puppy we don't know it's birthday. Pick the 
        # first dog's birthday plus one year. The SpeakText will be the concatenation
        # of both dog's text. The dog on the left side of the + operator is the object
        # referenced by the "self" parameter. The "otherdog" parameter is the dog on the right side of # the  +  operator.
    def __add__(self,otherDog):
            return Dog("Puppy of " + self.name + " and " + otherDog.name, self.month, self.day,self.year+ 1, self.speakText + otherDog.speakText)
        
def main():
    boyDog = Dog("Devil", 5, 15, 2017, "WOOFFFF")
    girlDog = Dog("someone", 5,6,2018,"barkbarkkkkk")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woohoooowohopooo")
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())


if __name__ == "__main__":
    main()

print("Stop")
tick = time.clock()
print(tick)