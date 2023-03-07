from plyer import notification
import schedule
import time

def Water_Reminder() :
    notification.notify(
    title = '# Water Reminder',
    message = 'Please drink a glass of water, you will feel fresh :)',
    app_icon = 'water.ico',
    timeout = 40,
    )
    print("Water")

def Medicine_Reminder() :
    notification.notify(
    title = '#Medicine Reminder',
    message = 'Its time for medicine , plz take your medicine !!',
    app_icon = 'medicine.ico',
    timeout = 40,
    )
    print("Medicine")

def Walk_Reminder() :
    notification.notify(
    title = 'Lets take a walk',
    message = 'Take a walk for 5 min its good for your health.',
    app_icon = 'walk.ico',
    timeout = 40,
    )
    print("Walk")

def main() :
    print("------------Reminder Application-----------")
    schedule.every(1).hours.do(Water_Reminder)
    schedule.every(2).hours.do(Medicine_Reminder)
    schedule.every(3).hours.do(Walk_Reminder)
    while True :
        schedule.run_pending()
        time.sleep(100)

if __name__ == "__main__" :
    main()