import datetime

with open("test.md", "a") as file :
    file.write(datetime.datetime.now())
