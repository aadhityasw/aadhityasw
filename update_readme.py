import datetime

with open("test.md", "a") as file :
    file.write(str(datetime.datetime.now()))
