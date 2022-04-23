"""Task 0.8"""

""" This function will convert time in minutes, to a more detailed layout with hours and minutes"""
def time(t):
    hours = (t // 60) 
    minutes = (t % 60)
    print((str(hours) + " hour") + " " + ( str(minutes) + " minutes") )

    
time(71)

print(("*" * 14) + "end")


