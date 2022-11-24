import sys
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import *
#from PyQt6.QtWidgets import QMainWindow, QApplication
from links_uteis import Ui_MainWindow
import webbrowser

def link_1():
    new=2
    url="https://www.linkedin.com/in/gleilsonpedro/"
    webbrowser.open(url,new=new)
def link_2():
    new=2
    url="https://github.com/gleilsonpedro"
    webbrowser.open(url,new=new)
    
def link_3():
    new=2
    url="https://replit.com/signup"
    webbrowser.open(url,new=new)

def link_4():
    new=2
    url="https://wiki.python.org.br/DocumentacaoPython"
    webbrowser.open(url,new=new)
    
def link_5():
    new=2
    url= "https://regex101.com"
    webbrowser.open(url,new=new)
    
def link_6():
    new=2
    url="https://stackoverflow.com"
    webbrowser.open(url,new=new)

   

class GUI_cont(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_component()
    
    def init_component(self):
        self.label_logo.setPixmap(QPixmap('img/gif_front.gif')) # importa a imagem
        self.setWindowIcon(QIcon('img/py_icon.ico')) # importa o icone
        
        self.bt_link_1.clicked.connect(link_1)
        self.bt_link_2.clicked.connect(link_2)
        self.bt_link_6.clicked.connect(link_6)
        self.bt_link_3.clicked.connect(link_3)
        self.bt_link_5.clicked.connect(link_5)
        self.bt_link_4.clicked.connect(link_4)
    
    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = GUI_cont()
    view.show()
    qt.exec()
    