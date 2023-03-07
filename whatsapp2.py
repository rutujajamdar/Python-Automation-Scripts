
# Import following modules
import time
import schedule
import openpyxl
import urllib.request
import pandas as pd  
from pushbullet import PushBullet


temp = 1
wb = openpyxl.Workbook()
ws = wb.active


def Task_lister() :
        Access_token = "o.YTOTS6wItzwYqHOswk0xCtPvlVONJc0p"
        global temp
        global wb
        global ws
        pb = PushBullet(Access_token)  # Authentication
        all_pushes = pb.get_pushes()  # All pushes created by you
        latest_one = all_pushes[0]  # Get the latest push
        url = latest_one['file_url']  # Fetch the latest file URL link

        Text_file = "All_Chats.txt"  # Create a new text file for storing all the chats
        # Retrieve all the data store into Text file
        urllib.request.urlretrieve(url, Text_file)

        chat_list = []  # Create an empty chat list

        # Open the Text file in read mode and read all the data
        with open(Text_file, mode='r', encoding='utf8') as f:
            data = f.readlines()  # Read all the data line-by-line

        # Excluded the first item of the list, coz first items contains some garbage data
        final_data_set = data[1:]

        # Run a loop and read all the data line-by-line
        i = 0 
        for line in final_data_set:
            if(i>=temp) :
                date = line.split(",")[0]  # Extract the date
                tim = line.split("-")[0].split(",")[1]  # Extract the time
                messag = line.split(":")[2].split("_")[0]  # Extract the message

                cost = line.split(":")[2].split("_")[1][:-1] # Extract the message
                
                chat_list = [date, tim,messag,cost]
                print("Data added is : ",chat_list)
                ws.append(chat_list)
            i = i +1

        temp = i
        wb.save("MyRecord.xlsx")

def main():
    schedule.every().thursday.at_time("10:30").do(Task_lister)
    while True :
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__" :
    main()