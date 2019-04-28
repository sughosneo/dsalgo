from CarManufactor import *

class Adapter(CarManufactor):

    def manufactoring(self):

        print("This is the generic manufactoring where acting as adapter for the BMW class manufactoring!")
        self._adaptee.specificManufacotoring()


