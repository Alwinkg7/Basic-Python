import datetime
x = datetime.date.today()
print(x)  #date
print(x.strftime("%d"))  #numday
print(x.strftime("%A"))  #day
print(x.strftime("%B %d, %Y"))  #month numday, year
print(x.strftime("%B %d, %Y %I:%M %p"))  #month numday, year time
print(x.strftime("%m"))  #nummonth
print(x.strftime("%a"))  #day eg sat
print(x.strftime("%y"))  #first 2 num of year
print(x.strftime("%b"))  #first 3 letter of month
print(x.strftime("%d"))  #num day
print(x.strftime("%I")) #hour
print(x.strftime("%I:%M %p")) #time
print(x.strftime("%p"))  #am or pm
print(x.strftime("%M")) #second