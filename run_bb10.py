__author__ = 'ASHISH'
import  sys
from bb10 import BB

def User():
    sys.stdout.write("\nGrabing Episode List:\n")
    global user_location, user_res , user_video
    start = BB()

    while True:
        try:
            user_video = int(input("\nEnter the number corresponding to the video name: ")) - 1
            user_location = input("\nEnter Download Location like this: Eg:- C:\\Downloads : ")
            sys.stdout.write("\nResolution :\n1.720p\n2.480p\n")
            user_res = int((input("Enter the number corresponding to resolution: "))) - 1
        except (ValueError,OSError):
            sys.stdout.write("\nPlease enter the values correctly")
            continue
        else:
            break
    start.down(user_video, user_res , user_location)
    input()

User()








