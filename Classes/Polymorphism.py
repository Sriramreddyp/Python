from abc import ABC, abstractmethod


class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Drawn a TextBox")


class DropDownListMenu(UIControl):
    def draw(self):
        print("Drawn a DropdownListMenu")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownListMenu()
# draw(ddl)
tb = TextBox()
# draw(tb)

draw([ddl, tb])
