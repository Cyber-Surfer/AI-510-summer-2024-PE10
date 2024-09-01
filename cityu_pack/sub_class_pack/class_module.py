class ClassModule:
    def __init__(self, global_init_param=None):
        self.global_init_param = global_init_param
        # we can also simply do a "pass" if we have nothing to initialize
        # pass
    
    def add(self, x,y):
        return x + y
    
    def multiply(self, x,y):
        return x * y