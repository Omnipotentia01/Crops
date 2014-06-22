import random

class Animal:
    """A generic animal"""

    #constructor
    def __init__(self, growth_rate, food_need, water_need):
        #set the attributes with initial values

        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "New Born"
        self._type = "Generic"
        self._name = None

        #attributes prefixed with an underscore to indicate that
        #they should not be accessed directly from outwith the class
    def needs(self):
        #returns dictionary containing food and water needs
        return {'food need':self._food_need,'water need':self._water_need}
    
    def report(self):
        #returns a dictionary containing the type, status, weight and days growing
        return{'name':self._name,'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing}

    def _update_status(self):
        if self._weight > 20:
            self._status = "Old"
        elif self._weight > 15:
            self._status = "Mature"
        elif self._weight > 8:
            self._status = "Young"
        elif self._weight > 3:
            self._status = "Baby"
        elif self._weight == 0:
            self._status = "New Born"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #inrement days_growing
        self._days_growing += 1
        #update the status
        self._update_status()

    

def auto_grow(animal, days):
    #grow the animal (0) for (1) days
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    #get the food and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print('Value entered in not not valid - Please only enter values between 1 and 10.')
        except ValueError:            
            print('Value entered in not not valid - Please only enter values between 1 and 10.')
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a waer value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                 print('Value entered in not not valid - Please only enter values between 1 and 10.')
        except ValueError:            
            print('Value entered in not not valid - Please only enter values between 1 and 10.')

       
def display_menu():
    print("1. Manually grow animal over one day")
    print("2. Automatically grow animal over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")    
        
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This allows you to manage your animals")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program. ")

def main():
    new_animal = Animal(1,4,3)
    manage_animal(new_animal)

if __name__ == "__main__":
    main()

    
