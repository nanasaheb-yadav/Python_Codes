"""
author: Nanasaheb, Yadav
Date: 18/06/2021
Description: This code is just to create timer which gives functions like Start, Pause, Reset.
Its very simple code just tried while practicing, anyone can update it if you have any short solutions.

"""

import os
import time

hrs = 0
minute = 0
secs = 0
while True:
    ip = int(input("Enter 1 to start \t"))
    if ip == 1:
        while True:
            ip_val = 0
            try:
                time.sleep(1)
                secs += 1
                if secs == 60:
                    minute += 1
                    secs = 0
                if minute == 60:
                    hrs += 1
                    minute = 0
                os.system('cls')
                print()
                print(f"              {hrs}: {minute}: {secs}")
                print("\tPress 'ctrl+c' to pause")
            except KeyboardInterrupt:
                ip_val = int(input("Press Keys to \n Start: 1  \t Reset: 4 \t"))
                if ip_val == 1:
                    if ip_val == 1:
                        continue
                    else:
                        time.sleep(100)
                elif ip_val == 4:
                    hrs = minute = secs = 0
                    break
                else:
                    pass
    else:
        pass
