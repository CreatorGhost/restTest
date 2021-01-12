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
