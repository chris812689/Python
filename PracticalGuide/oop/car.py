class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, top_speed =100):
        self.top_speed = top_speed
        self.__warnings = []
    
    def __reper__():
        return 'Top speed : '

    def add_warning(self,warning_text):
        if len(warning_text) >0:
            self.__warnings.append(warning_text)

    def drive(self):
        print('I am driving')

car1 = Car()
  