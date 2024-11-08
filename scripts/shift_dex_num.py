import os

#shift dex numbers from start to stop by the amount given. Run in poke folder.
#start including stop including amount int
def shift_num(start,stop,amount,up = True):
    count = 0
    if not up:
        amount *= -1
    for file in os.listdir():
        if file.endswith(".txt") and file.startswith("OUTLINE") == False:
            f = open(file,"r")
            data = f.readlines()
            if len(data) > 8:
                num = int(data[8])
                if num >= start and num <= stop:
                    if num == start:
                        print("start with "+file[:-4])
                    if num == stop:
                        print("end with "+file[:-4])
                    data[8] = str(num + amount) + "\n"
                    count += 1
                f = open(file,"w")
                f.writelines(data)
            f.close()
    print(str(count) + "files changed.")

def read_file():
    for file in os.listdir():
        if file.endswith(".txt") and file.startswith("OUTLINE") == False:
            f = open(file,"r")
            data = f.readlines()
            print(data[8])
            f.close()
            return

if __name__ == "__main__":
    #read_file()
    #trevenant
    #shift_num(114,180,-2)
