from editor import Editor
from history import History
from converter_p10 import Conver_P_10
from converter_10p import Conver_10_P

class Control:
    def __init__(self):
        self.pin = 10
        self.pout = 16
        self.state = "Редактирование"
        self.editor = Editor()
        self.history = History()

    def do_command(self, j: int) -> str:
        """
        Выполняет команду.
        """
        if j == 19:
            r = Conver_P_10.dval(self.editor.number, self.pin)
            res = Conver_10_P.do(r, self.pout, 3)
            self.state = "Преобразовано"
            self.history.add_record(self.pin, self.pout, self.editor.number, res)
            return res
        else:
            self.state = "Редактирование"
            return self.editor.do_edit(j)