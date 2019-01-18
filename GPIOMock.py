"""class GPIOMock:
    @classmethod
    def output(self, port, state):
        print("set " + str(port) + " to " + str(state))

    @staticmethod
    def cleanup(self, port):
        print("cleanup " + str(port))"""
    
    
def cleanup(port):
    print("cleanup " + str(port))
    
def output(port, state):
    print("set " + str(port) + " to " + str(state))