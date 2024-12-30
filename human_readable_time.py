from datetime import time
def human_readable_time(seconds: int)-> time:
    hours = int(seconds / 3600) 
    
    remainder = int(seconds % 3600)
   
    minutes, seconds = int(remainder / 60), int(remainder % 60)

    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

def main()-> None:
    print((human_readable_time(3600)))

if __name__ =="__main__":
    main()