import sys
import pandas as pd

if __name__ == "__main__":

    print(sys.argv)
    
    if len(sys.argv) < 3:
        print('Sys.argv ---------------error')
    else:
        try:
            print("Split ---------------start")
            v_list = pd.read_csv(sys.argv[1], \
                         sep ='\t', \
                         header=0, \
                         engine='python', quotechar='"', error_bad_lines=False, \
                         skip_blank_lines=True)
        
            start = 0
            end = int(sys.argv[3]) - 1
            last = len(v_list)
        
            while start < last:
                a_list = v_list.loc[start:end]
                a_list.to_csv(sys.argv[2] + 'out_' + str(start+1) + '.csv', index=None)
                start = end + 1
                end = start + int(sys.argv[3]) - 1
            
                #print(a_list)
            print("Split ---------------end")
        except Exception as e:
            print('Split ---------------error')
            print(e)

    