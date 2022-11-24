import sys
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import *
#from PyQt6.QtWidgets import QMainWindow, QApplication
from links_uteis import Ui_MainWindow
import webbrowser

def painel():
    new=2
    url="http://10.27.2.122/svo/public/login"
    webbrowser.open(url,new=new)
def entrada():
    new=2
    url="http://extranet.saude.ce.gov.br/svo/logon.jsp?sys=SVO"
    webbrowser.open(url,new=new)
    
def ponto():
    new=2
    url="http://extranet.saude.ce.gov.br/mjp/login/"
    webbrowser.open(url,new=new)

def almoxarifado():
    new=2
    url="http://almox.saude.ce.gov.br/almox/login.jsf"
    webbrowser.open(url,new=new)
    
def pontoweb():
    new=2
    url= "http://sistemas.saude.ce.gov.br/pwb/pages/batida.jsf"
    webbrowser.open(url,new=new)
    
def gal():
    new=2
    url="https://gal.saude.ce.gov.br/gal/"
    webbrowser.open(url,new=new)

def entrada():
    new=2
    url="http://extranet.saude.ce.gov.br/svo/logon.jsp?sys=SVO"
    webbrowser.open(url,new=new)
    
def ponto():
    new=2
    url="http://extranet.saude.ce.gov.br/mjp/login/"
    webbrowser.open(url,new=new)

def almoxarifado():
    new=2
    url="http://almox.saude.ce.gov.br/almox/login.jsf"
    webbrowser.open(url,new=new)
    
def pontoweb():
    new=2
    url= "http://sistemas.saude.ce.gov.br/pwb/pages/batida.jsf"
    webbrowser.open(url,new=new)
    
def gal():
    new=2
    url="https://gal.saude.ce.gov.br/gal/"
    webbrowser.open(url,new=new)    

class GUI_cont(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_component()
    
    def init_component(self):
        self.label_logo.setPixmap(QPixmap('img/gif_front.gif')) # importa a imagem
        self.setWindowIcon(QIcon('img/py_icon.ico')) # importa o icone
        
        self.bt_chamados.clicked.connect(painel)
        self.bt_entrada.clicked.connect(entrada)
        self.bt_ponto.clicked.connect(ponto)
        self.bt_almox.clicked.connect(almoxarifado)
        self.bt_ponto_2.clicked.connect(pontoweb)
        self.bt_gal.clicked.connect(gal)
    
    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = GUI_cont()
    view.show()
    qt.exec()
    