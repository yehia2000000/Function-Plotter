##############################################################################
##############################################################################
#####################    yehia ahmed Ibrahim      ############################
#####################    Plot Function            ############################
#####################    21/12/2021               ############################
##############################################################################
##############################################################################


###########################Define the library##################################
import ntpath
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.uic import loadUiType
import sys
import os
import matplotlib.pyplot as mp
import numpy as nu




###########################Define the QT design ###############################

FormClass,_ = loadUiType (ntpath.join(ntpath.dirname(__file__),"PlotFunction.ui"))



class MainWindow  (QWidget,FormClass):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()


    def Handle_UI (self):
        self.setWindowTitle("Plot Function")
        self.setFixedSize(481,250)

    def Handle_Buttons (self):
        self.pushButton.clicked.connect (self.Handle_Plot)

    def Handle_Plot (self):
        try :
            order =[]
            coff = []
            Function = self.lineEdit.text()
            Function_Split = Function.split('+')
            print (Function_Split)
            for count in range (0,len(Function_Split)):
                try:
                    print(Function_Split[count][-1])
                    if Function_Split[count][-1] =='x':
                        order.append(1)
                    elif Function_Split[count][-2] =='^':
                        order.append(int(Function_Split[count][-1]))
                except :
                    order.append(0)
            AddedValue = ''
            for count in range (0,len(Function_Split)):
                if Function_Split[count][0] == 'x':
                    coff.append(1)
                else:
                    for i in range (0,len(Function_Split[count])):
                        if Function_Split[count][i] != 'x'and Function_Split[count][i] != '*':
                            AddedValue = AddedValue +Function_Split[count][i]
                        else :
                            coff.append(int(AddedValue))
                            AddedValue = ''
                            break
                        if (i == len(Function_Split[count])-1):
                            coff.append(int(AddedValue))
            order.append(0)
            coff.append(0)
            Fun =0
            Max = int(self.lineEdit_4.text())
            Min = int(self.lineEdit_2.text())
            x= nu.linspace(Min,Max,num=1000)
            for count in range (0,len(coff)-1):
                Fun = Fun + coff[count]*(x**order[count])
            print (order)
            print (coff)
            mp.figure(num=0,dpi=100)
            mp.plot(x,Fun)
            mp.show()
        except :
            QMessageBox.warning(self, "Not Completed Plot", "the plot is not finished")

def main ():
    app =QApplication(sys.argv)
    Main_Loop = MainWindow ()
    Main_Loop.show()
    app.exec()

if __name__ == '__main__':
    main()