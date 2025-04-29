from modules import clean
from modules import demo


class Wrapper:
    def __new__(self, module_name):
        if module_name == "clean":
            return clean
        else:
            return demo
