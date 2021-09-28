import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P5_PromedioN_lista.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_operacion.clicked.connect(self.operacion)

        self.btn_operacion.setText("COMENZAR")

        self.txt_calif.setEnabled(False)
        self.txt_calif_actual.setEnabled(False)
        self.txt_resultado.setEnabled(False)

        self.n = -1
        self.lista = [] #LISTA VACIA

    #area de slots
    def operacion(self):
        op = self.btn_operacion.text()

        if op=="COMENZAR":
            self.btn_operacion.setText("AÑADIR")

            self.n = int(self.txt_n.text())

            self.txt_calif.setEnabled(True)
            self.txt_calif_actual.setText("1")
            self.txt_n.setEnabled(False)

        elif op=="AÑADIR":

            #print(self.n)
            calif_actual = int(self.txt_calif_actual.text()) #contador

            if calif_actual<=self.n:

                calif = float(self.txt_calif.text())
                self.lista.append(calif)
                print(self.lista)

                calif_actual += 1

                self.txt_calif.setText("") # para borrar la calif ingresada

                if calif_actual == self.n+1:
                    self.btn_operacion.setText("CALCULAR")
                    self.txt_calif.setEnabled(False)
                else:
                    self.txt_calif_actual.setText(str(calif_actual))

        else: #PRocedimiento a realizar cuando se precia el "calcular"
            self.btn_operacion.setText("COMENZAR")

            suma = sum(self.lista)

            prom = suma/len(self.lista)

            prom = round(prom, 3)

            self.txt_resultado.setText(str(prom))

            self.lista.clear()

            self.txt_n.setEnabled(True)


    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())