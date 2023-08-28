import data_import as di

class Manager:

    def __init__(self):
        self.actions = {}

    def assign(self, name):
        # method to assign tasks to appropriate operations in the accounting system
        def inner_function(func):
            self.actions[name] = func

        return inner_function
    
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Command not defined. Please enter available command\n.")

        else:
            self.actions[name](*args, **kwargs)




