import subprocess
try:
    subprocess.check_call('dtir',shell=True)
except subprocess.CalledProcessError as e:
    print(f'Command failed with error: {e}')

import multi
import multiprocessing
if __name__=='__main__':
    p3=multiprocessing.Process(target=multi.prints,args=('C'))
    p3.start()
    p3.join()
    print('process ended')

