import os
import shutil
if not os.path.exists('learn'):
    os.makedirs("learn")

    with open("learn/source.txt",'w') as file:
        file.write("Hello. WElcome!")

    shutil.copy2("learn/source.txt","learn/destination.txt")
    shutil.move('learn/destination.txt','learn/move.txt')
    shutil.copytree('learn','learnt')
shutil.copystat('learn','main.py')