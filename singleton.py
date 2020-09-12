class singleton:
    __instance_variable="uninvoked"
    def __init__(self):
        if singleton.__instance_variable=="uninvoked":
            singleton.__instance_variable=self
        else:
            raise Exception("duplicate instance")
    @staticmethod
    def get_instance():
        if singleton.__instance_variable=="uninvoked":
            singleton()
            return singleton.__instance_variable

        else:
            return singleton.__instance_variable


firstTime=singleton()
print(firstTime)
firstTime.get_instance()
print(firstTime.get_instance())
