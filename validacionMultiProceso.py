import os
from time import sleep
from datetime import datetime

def padre():
    try:

        for i in range(10):

            newpid = os.fork()

            if newpid == 0:
                horaActual = datetime.now().time().strftime("%H:%M:%S")

                print("\n>><< Iniciando el proceso: {} a las {}".format(os.getpid(), horaActual))
                hijo()

            sleep(10)

    except:
        print("Ha ocurrido un error, inténtelo más tarde")


def hijo():

    print(">><< Iniciando el proceso con PID: {}".format(os.getpid()))
    sleep(3)
    print(">><< Terminando el proceso con PID: {}\n".format(os.getpid()))
    os._exit(0)

if __name__ == "__main__":
    padre()
