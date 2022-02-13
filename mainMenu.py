from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

import sys
import snap7
from snap7.util import *
from snap7.types import *

from UI_ScadaSystem import Ui_ScadaSystem


class ScadaSystem_App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ScadaSystem_App, self).__init__()
        self.ui = Ui_ScadaSystem()
        self.ui.setupUi(self)

        self.plc1 = snap7.client.Client()
        self.plc1.connect('PLC IP ADDRESS 1',0,1)          #Atik Su Terfi 2

        self.plc2 = snap7.client.Client()           
        self.plc2.connect('PLC IP ADDRESS 2',0,1)          #Atik Su Terfi 1

        self.plc3 = snap7.client.Client()               
        self.plc3.connect('PLC IP ADDRESS 3',0,1)          #Atik Su Aritma

        timer = QTimer(self)
        timer.timeout.connect(self.Stations)
        timer.start(100)


    def Stations(self):

        def AtikSuTerfi2():                                         #PLC IP ADDRESS 1
            database = self.plc1.db_read(1,0,24)

            current_level = snap7.util.get_real(database,4)         #su yuksekligi
            total_volume = snap7.util.get_real(database,8)          #su kapasitesi
            current_volume = snap7.util.get_real(database,12)       #mevcut su hacmi
            water_fillrate = (current_volume/total_volume)*100      #doluluk orani

            self.ui.txt_AtikSuTerfi2_SY.setText(str(float("{:.5f}".format(current_level))))
            self.ui.txt_AtikSuTerfi2_SK.setText(str(int(total_volume)))
            self.ui.txt_AtikSuTerfi2_DO.setText(str(float("{:.2f}".format(water_fillrate))))
            self.ui.txt_AtikSuTerfi2_SH.setText(str(int(current_volume)))
        

        def AtikSuTerfi1():                                         #PLC IP ADDRESS 2
            database = self.plc2.db_read(1,0,20)
 
            current_level = snap7.util.get_real(database,4)         #su yuksekligi
            total_volume = snap7.util.get_real(database,8)          #su kapasitesi
            current_volume = snap7.util.get_real(database,12)       #mevcut su hacmi
            water_fillrate = (current_volume/total_volume)*100      #doluluk orani

            self.ui.txt_AtikSuTerfi1_SY.setText(str(float("{:.5f}".format(current_level))))
            self.ui.txt_AtikSuTerfi1_SK.setText(str(int(total_volume)))
            self.ui.txt_AtikSuTerfi1_DO.setText(str(float("{:.2f}".format(water_fillrate))))
            self.ui.txt_AtikSuTerfi1_SH.setText(str(int(current_volume)))


        def AtikSuAritma():                                         #PLC IP ADDRESS 3 
            database = self.plc3.db_read(1,0,20)
 
            current_level = snap7.util.get_real(database,2)         #su yuksekligi
            total_volume = snap7.util.get_real(database,6)          #su kapasitesi
            current_volume = snap7.util.get_real(database,10)       #mevcut su hacmi
            water_fillrate = (current_volume/total_volume)*100      #doluluk orani

            self.ui.txt_AtikSuAritma_SY.setText(str(float("{:.5f}".format(current_level))))
            self.ui.txt_AtikSuAritma_SK.setText(str(int(total_volume)))
            self.ui.txt_AtikSuAritma_DO.setText(str(float("{:.2f}".format(water_fillrate))))
            self.ui.txt_AtikSuAritma_SH.setText(str(int(current_volume)))

        AtikSuTerfi2()
        AtikSuTerfi1()
        AtikSuAritma()

def app():
    app = QtWidgets.QApplication(sys.argv)  
    win = ScadaSystem_App()
    win.showFullScreen()
    sys.exit(app.exec_())

app()
    

