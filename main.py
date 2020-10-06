# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#          .----.   @   @                    _ _   www.github.com/snailware   #
#         / .-"-.`.  \v/     ___ _ __   __ _(_) |_      ____ _ _ __ ___       #
#         | | '\ \ \_/ )    / __| '_ \ / _` | | \ \ /\ / / _` | '__/ _ \      #
#       ,-\ `-.' /.'  /     \__ \ | | | (_| | | |\ V  V / (_| | | |  __/      #
#      '---`----'----'      |___/_| |_|\__,_|_|_| \_/\_/ \__,_|_|  \___|      #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                      #                                      #
#            Adam Lancaster            #              Quick Timer             #
#            10 / 05 / 2020            #   easy to operate, multi-use timer   #
#                                      #                                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#       program will take accept input times in the form of a set time, or    #
#   interval. at desired time, program will produce a pop up window and play  #
#   a sound effect to alert user.                                             #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import datetime
import time
import sys
import pyautogui as pag
from playsound import playsound

pag.FAILSAFE = False
# failsafe is disabled to allow program to run in background without being
# accidently closed by user.

def main():

    selection = methodSelect()

    if selection == 'manual time entry':

        manualTimer()

    else:

        intervalTimer()

    sys.exit()

def methodSelect():
# function will display a window prompting user to select 'manual entry' or 
# 'interval' based timing. if window is closed, it will immediately reopen.
# user MUST select one of the choices to continue execution. 

    option1 = 'manual time entry'
    option2 = 'interval based'
    # set input choices. 

    selection = 'None'
    while selection != option1 and selection != option2:
        selection = pag.confirm('select timing method:', 'method selection',
                                buttons = [option1, option2])
    return selection
    # input validation loop. 

def manualTimer():
# timer will prompt user to enter a time, then alert user at desired time. 

    currentTime     = datetime.datetime.now()
    currentHour     = currentTime.hour
    currentMinute   = currentTime.minute
    # get current time. 

    chosenHour = -1
    while chosenHour < 0 or chosenHour > 23:
        try:
            chosenHour = int(pag.prompt('enter alert hour: (0 - 23)', 
                                        'hour prompt', currentHour))
        except:
            pass
    # input validation and error handling for chosenHour input.

    chosenMinute = -1
    while chosenMinute < 0 or chosenMinute > 59:
        try:
            chosenMinute = int(pag.prompt('enter alert minute: (0 - 59', 
                                        'minute prompt', currentMinute))
        except:
            pass
    # input validation and error handling for chosenMinute input. 
    
    while chosenHour != currentHour or chosenMinute != currentMinute: 
        time.sleep(1)
        currentTime     = datetime.datetime.now()
        currentHour     = currentTime.hour
        currentMinute   = currentTime.minute
    # wait until desired alert time and then proceed with execution. 
        
    alert()
    # display alert message. 

def intervalTimer():
# timer will prompt user to enter the amount of time in minutes to wait for,
# then alert user at desired time. 

    timerInterval = -1
    while timerInterval < 0:
        try:
            timerInterval = float(pag.prompt('enter alert interval in mins:',
                                            'interval prompt', 'XXX'))
        except:
            pass
    # input validation and error handling for interval input.

    time.sleep(timerInterval * 60)
    # wait for the desired amount of time. 

    alert()
    # display alert message. 

def alert():
# function will display an alert message, notifying user that time is up. 

    pag.alert('time is up!', 'alert', 'OK')
    # displays alert message. 

main()