from module import myFunc
#connected to the module.py

if __name__=="__main__":
    #if this code is directly executed by running the file its present in

    print("We are directly running this code")
    myFunc()
    print(__name__)