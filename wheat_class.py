from cropclass import *

class Wheat(Crop):
    """ A representaion of a wheat crop"""
    #Constructor
    def __init__(self):
        #Call super constructor
        super().__init__(1,3,6)
        self._type = "Wheat"

    #Override previous methods for subclass (grow in this case)
        def grow(self,light,water):
            if light >= self._light_need and water >= self._water_need:
                if self._status == "Seedling" and water > self._water_need:
                    self.growth += self._growth_rate * 1.5
                elif self._status == "Young" and water > self.water_need:
                    self._growth += self._growth_rate *1.25
                elif self._status == "Old" and water > self.water_need:
                    self._growth += self._growth_rate / 2               
                else:
                    self._growth += self._growth_rate
            #increment day growing
            self._days_growing += 1
            #update status
            self._update_status()

def main():
    #Create Wheat crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #manualy grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())            

if __name__ == "__main__":
    main()
