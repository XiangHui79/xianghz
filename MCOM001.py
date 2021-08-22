# -*- coding: utf-8 -*-

from amz.rbs.vsp.mvm.win.bas import WBAS001,WBAS901
from amz.rbs.vsp.mvm.func.com import FCOM001, FCOM002, FCOM003
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QApplication
import time

#-------------------------------------------
# Start method of the MVM operation system                 
# Version : 1.0                             
# Owner   : @xianghz                        
# Update  : 2019-01-24                      
#-------------------------------------------
if __name__ == "__main__":
    #Initiate the whole Application
    import sys, os
    
    #Start the Application process
    app = QtWidgets.QApplication(sys.argv)

    #Show the welcome window
    ui_bas901 = WBAS901.Ui_WBAS901()
    ui_bas901.gcShow()
    QApplication.processEvents()
    time.sleep(1)
    
    #dirname, filename = os.path.split(os.path.abspath(__file__))
    __currentPath = 'C:\OMS'

    if FCOM003.initProperty(__currentPath,"Oms.conf",__currentPath + os.sep + "Log") == FCOM001.STATUS_000 and \
       FCOM003.initMailProperty(__currentPath,"Mail.conf") == FCOM001.STATUS_000 and \
       FCOM003.initTableProperty(__currentPath,"TblDf.conf") == FCOM001.STATUS_000 and \
       FCOM003.initBasicProperty(__currentPath,"Oms_B.conf") == FCOM001.STATUS_000:
        __log = FCOM002.LOG
        __log.out.info("Start: OM-System")

        #Show the Top window
        ui_bas001 = WBAS001.Ui_WBAS001()
        ui_bas901.close()
        ui_bas001.show()

        __log.out.info("End: OM-System")
    else:
        ui_bas901.close()
        print('[ERROR] The main process has ended')
     
    #Hold the Application process    
    sys.exit(app.exec_())