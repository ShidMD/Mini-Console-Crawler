import time
import os

def delay_10ms():
    time_start = time.time()
    a = 1999999
    while a > 0:
        a -= 1
    time_finish = time.time()
    print(time_finish - time_start)

class Charmander:
    n
    ame = str(None)

class TerminalDisplay:
    columns = None
    lines = None
    def get_size(self):
        self.columns,self.lines = os.get_terminal_size()



json = {"name":"Nathin",
'dymorph':False;}



class Foo:
    @staticmethod
    def function_dum():
        print(type(1))
        return None

    @staticmethod
    def ducntion_fum() -> None:
        print(type(.0))


Foo.function_dum()
Foo.ducntion_fum()