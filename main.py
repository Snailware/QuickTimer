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
# accidently closed but user.

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

    selection = 'None'
    while selection != option1 and selection != option2:
        selection = pag.confirm('select timing method:', 'method selection',
                                buttons = [option1, option2])
    return selection

def manualTimer():
# timer will prompt user to enter a time, then alert user at desired time. 

    currentTime     = datetime.datetime.now()
    currentHour     = currentTime.hour
    currentMinute   = currentTime.minute

    chosenHour      = int(pag.prompt('enter alert hour:', 'hour prompt', 
                                    currentHour))
    chosenMinute    = int(pag.prompt('enter alert minute:', 'minute prompt', 
                                    currentMinute))
    
    if chosenHour == currentHour and chosenMinute == currentMinute:

        alert()

def intervalTimer():
# timer will prompt user to enter the amount of time in minutes to wait for,
# then alert user at desired time. 

    timerInterval = int(pag.prompt('enter alert interval in minutes:',
                                  'interval prompt', 'XXX'))

    time.sleep(timerInterval * 60)

    alert()

def alert():
# function will display an alert message, notifying user that time is up. 

    pag.alert('time is up!', 'alert', 'OK')

main()