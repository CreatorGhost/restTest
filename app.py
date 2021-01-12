from flask import Flask,jsonify,request
#from ckeck import chk
app = Flask(__name__)
import threading 
from time import sleep
import os

def remove():
    while True:
        try:
            file=open('exit')
            file.close()
            os.remove('exit')
            exit()
        except IOError:
            pass


def keepRunning():
    a=0
    while True:
        sleep(5)
        print('Sending Data......')
        a+=1
        if a==4:
            break


@app.route('/add/',methods=['GET','POST'])
def add():
    if request.method=='GET':
        data=request.args.to_dict()
        temp=[]
        for i in data.values():
            temp.append(int(i))
        result={
            "sum":sum(temp)
        }

    return jsonify(result)

if __name__ == "__main__": 
	app.run()