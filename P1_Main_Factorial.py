import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_Factorial.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)

   # Área de los Signals
    self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):

        num = int(self.txt_num.text())
        resultado = num * (num-1)
        for i in range(num - 2, 0, -1):
         resultado = str(resultado * i)

   # print(result)

    #self.txt_resultado.setText(result)
    def mensaje (self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
