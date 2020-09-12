
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
