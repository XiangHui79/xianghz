import os,sys
import subprocess
import configparser as co

if __name__ == "__main__":
    
    flg = True
    folder = sys.argv[1]
    file = sys.argv[2]

    if not os.path.exists(folder + os.sep + file):
        flg = False
        
    if flg == True:
        flg = False
        cf = co.ConfigParser()
        cf.read(folder + os.sep + file, encoding='ANSI')
        items = cf.items('version')
        del cf
        
        cf = co.ConfigParser()
        cf.read('C:\OMS\ini\Oms_B.conf', encoding='ANSI')
        current = cf.get('B', 'ver').split('.')
        cr = ('0'+current[0])[-2:] + ('0'+current[1])[-2:] + ('0'+current[2])[-2:]
        del cf,current
        
        for section in items:
            key = section[0]
            if key > cr:
                flg = True
                break
        del items,cr
                
        if flg == True:
            # Start up the version up tracking method
            subprocess.run('C:\OMS\op\MCOM003.exe "' + folder + '" ' + file, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Start up the normal OMS
    subprocess.run("C:\OMS\op\MCOM001.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
