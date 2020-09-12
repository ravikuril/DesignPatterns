
class language1:
    def __init__(self):
        self.__language1_list=['l1.1','l1.2','l1.3']
    def get_list(self):
        return language1().__language1_list

class language2:
    def __init__(self):
        self.__language2_list=['l2.1','l2.2','l2.3']
    def get_list(self):
        return language2().__language2_list

class language3:
    def __init__(self):
        self.__language3_list=['l3.1','l3.2','l3.3']
    def get_list(self):
        return language3().__language3_list


class language_selector:

    def __init__(self):
        self.__language_object_dict={"language1":language1,"language2":language2,"language3":language3}
    def factory(self,language:str):
        return self.__language_object_dict[language]()

print(language_selector().factory("language1").get_list())
print(language_selector().factory("language2").get_list())
print(language_selector().factory("language3").get_list())



"""
Advantages of using Factory method:

    We can easily add the new types of products without disturbing the existing client code.
    Generally, tight coupling is being avoided between the products and the creator classes and objects.

Disadvantages of using Factory method:

    To create a particluar concrete product object, client might have to sub-class the creator class.
    You end up with huge number of small files i.e, cluttering of the files.
    Applicability :
        In a Graphics system, depending upon the user’s input it can draw different shapes like Rectangle, Square, Circle, etc. But for the ease of both developers as well as the client, we can use the factory method to create the instance depending upon the user’s input. Then we don’t have to change the client code for adding a new shape.
        In a Hotel booking site, we can book a slot for 1 room, 2 rooms, 3 rooms, etc. Here user can input the number of rooms he wants to book. Using the factory method, we can create a factory class AnyRooms which will help us to create the instance depending upon the user’s input. Again we don’t have to change the client’s code for adding the new facility.

"""
