class Washing: 
    '''Subsystem # 1'''
  
    def wash(self): 
        print("Washing...") 
  
  
class Rinsing: 
    '''Subsystem # 2'''
  
    def rinse(self): 
        print("Rinsing...") 
  
  
class Spinning: 
    '''Subsystem # 3'''
  
    def spin(self): 
        print("Spinning...") 
  
  
class WashingMachine: 
    '''Facade'''
  
    def __init__(self): 
        self.washing = Washing() 
        self.rinsing = Rinsing() 
        self.spinning = Spinning() 
  
    def startWashing(self): 
        self.washing.wash() 
        self.rinsing.rinse() 
        self.spinning.spin() 
  
""" main method """
if __name__ == "__main__": 
  
    washingMachine = WashingMachine() 
    washingMachine.startWashing() 
    
    
    
    
 """
 Advantages

    Isolation: We can easily isolate our code from the complexity of a subsystem.
    Testine Process: Using Facade Method makes the process of testing comparitively easy since it has convenient methods for commmon testing tasks.
    Loose Coupling: Availability of loose coupling between the clients and the Subsytems.

Disadvantages

    Changes in Methods: As we know that in Facade method, subsequent methods are attached to Facade layer and any change in subsequent method may brings change in Facade layer which is not favourable.
    Costly process: It is not cheap to establish the Facade method in out application for the system reliability.
    Violation of rules: There is always the fear of violation of the construction of the facade layer.

Applicability

    Providing simple Interface: One of the most important application of Facade Method is that it is used whenever you want to provide the simple interface to the complex sub-system
    Division into layers: It is used when we want to provide a unique structure to a sub-system by dividing them into layers. It also leads to loose coupling between the clients and the subsystem.

 """
