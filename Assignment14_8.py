class vehicle:
    def start(self):
        print("This is base claas method")

class car(vehicle):
    def start(self):
        print("This is derived class method ")

def main():
    vobj = vehicle()
    cobj = car()

    vobj.start()
    cobj.start()

if __name__=="__main__":
    main()

    
