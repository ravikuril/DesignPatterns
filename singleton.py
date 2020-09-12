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







"""
Advantages of using Singleton Method:

    Initializations: Object created by Singleton method is initialized only when it is requested for the first time.
    Access to the object: We got the global access to the instance of the object.
    Count of instances: In singleton method classes can’t have more than one instance

Disadvantages of using Singleton Method:

    Multithread Environment: Its not easy to use the singleton method in multithread environment, because we have to take care that multithread wouldn’t create singleton object several times.
    Single responsibility Principle: As the Singleton method is solving two problems at a single time, it doesn’t follow the single responsibility principle.
    Unit testing process: As they introduce the global state to the application, it makes the unit testing very hard.

Applicability

    Controlling over global variables: In the projects where we specifically need the strong control over the global variables, it is highy recommended to use Singleton Method
    Daily Developers use: Singleton patterns are generally used in providing the logging, caching, thread pools and configuration settings and oftenly used in conjuction with Factory design pattern.

"""
