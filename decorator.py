class base:
    __base_variable="Not_initiated"
    def __init__(self):
            self.__base_variable="INIT"
    def print1(self):
        return "{}".format(self.__base_variable)
class layer1(base):
    def __init__(self,shared_object_from_base):
        self._layer1_var=shared_object_from_base
    def print1(self):
        return "<l1>{}</l1>".format(self._layer1_var.print1())

class layer2(base):
    def __init__(self,shared_object_from_layer1):
        self._layer2_var=shared_object_from_layer1
    def print1(self):
        return "<l2>{}</l2>".format(self._layer2_var.print1())

class layer3(base):
    def __init__(self,shared_object_from_layer2):
        self._layer3_var=shared_object_from_layer2
    def print1(self):
        return "<l3>{}</l3>".format(self._layer3_var.print1())


layered_object=layer3(layer2(layer1(base())))
print(layered_object.print1())
