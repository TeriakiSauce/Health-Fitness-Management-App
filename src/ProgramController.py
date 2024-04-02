from DatabaseModel import Model
from GUIView import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        self.view.main()
    
if __name__ == "__main__":
    calculator = Controller()
    calculator.main()
    