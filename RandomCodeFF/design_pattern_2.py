# Creational Patterns _ Singleton

# objA, objB, objC, objD -> singleton - shared resource - stored state

# APP gives output to Child1, Child2 and Provider 
# child 2 gives output to Child3, Child4 
# provider gives output to Store
# Child1, Child2, Child3, Child4 were stored in Store as well

class ApplicationState:
    instance = None 

    def __init__(self):
        self.isLoggedIn = False 

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    
appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn) # False 

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True 

print(appState1.isLoggedIn) # True 
print(appState2.isLoggedIn) # True