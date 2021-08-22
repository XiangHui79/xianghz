# -*- coding: utf-8 -*-

from amz.rbs.vsp.mvm.win.bas import WBAS903
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QApplication

#-------------------------------------------
# Start method of the MVM operation system - new version tracking method               
# Version : 1.0                             
# Owner   : @xianghz                        
# Update  : 2020-05-24                      
#-------------------------------------------
if __name__ == "__main__":
    #Initiate the whole Application
    import sys
    
    folder = sys.argv[1]
    file = sys.argv[2]
    
    #Start the Application process
    app = QtWidgets.QApplication(sys.argv)

    #Show the welcome window
    ui_bas903 = WBAS903.Ui_WBAS903(folder, file)
    ui_bas903.gcShow()
    QApplication.processEvents()

    #Hold the Application process    
    sys.exit(app.exec_())