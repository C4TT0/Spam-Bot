import pyautogui
from time import sleep, time
import sys

print("[+] This will send spam messages in every 0.2 second. Press Ctrl + C to stop the execution")
sleep(1)

msg = str(input("[+] Enter message to spam: "))

print("[+] Take your cursor to the input where you have to spam")
sleep(1)

print("[+] Beggining Spam in 5 Seconds")
sleep(5)

counter = 0
i = 0

start_time = time()

try:
    while True:
        pyautogui.write(msg)
        pyautogui.hotkey('enter')
        sleep(0.2)
        counter += 1
except KeyboardInterrupt:
    print("[-] Stopping Execution")
    print("[+] Total Spam message sent : " + str(counter))
    print("[+] Total time of spam: " + str(time() - start_time) + " seconds")
    sys.exit(0)

