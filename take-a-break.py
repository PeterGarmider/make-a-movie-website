import webbrowser
import time

total_breaks = 3
break_counter = 0

print("This program has started on "+ time.ctime())
while break_counter < total_breaks:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=AaiaXmg33JU")
    break_counter = break_counter + 1
