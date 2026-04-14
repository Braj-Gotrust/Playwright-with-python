# ABC = Abstract Base Class
# ABC is inbuild class

# Given the functionality but hiding the implementation is call abstraction

from abc import ABC,abstractmethod
# abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class ( Implemented abstract method from abstract class )
class Car(Vehicle):
    def start(self):
        print("car engine start")

    def stop(self):
        print("car engine stop")

# v_obj = Vehicle()   # We can not create object of the abstract class
# v_obj.start()
# v_obj.stop()

c_obj = Car()
c_obj.start()
c_obj.stop()