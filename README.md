
Problem Statement:
Using any preferred language create a method which will read the strArr parameter being passed which will
represent a full day and will be filled with events that span from time X to time Y in the day. The format of each
event will be hh:mm AM/PM- hh:mm AM/PM.
For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM09:50AM"].
Your program will have to output the longest amount of free time available between the
start of your first event and the end of your last event in the format: hh:mm. The start
event should be the earliest event in the day and the latest event should be thelatest
event in the day.
The output for the previous input would therefore be 01:30 (with the earliest event in the
day starting at 09:10AM and the latest event ending at 02:45PM). The input will contain
at least 3 events and the events may be out of order.

Input:
 ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM09:50AM"]
 
Output:

01:30

STEPS:
1. Take the events list as input from user.
2. arrange those events asssending order
3. covert the events into miniutes from hr:mm format
4. iterate thought all events and using diffrence calulate free time and keep maximum free time in most_free variable
5.covert this most_free time into hr:mm format
6.print output


<img src="/shagun%20out.JPG"/>

CODE:[Python 3]

def turn_into_minutes(time):
  result = time[:-2].split(":") 
  result = [int(result[0]), int(result[1])] if time[-2:] == "AM" else [int(result[0])+12, int(result[1])]
  result[0] = result[0] if (result[0]!=12 and result[0]!=24) else result[0]-12
  return result[0] * 60 + result[1]

def MostFreeTime(strArr): 
  times_l = []
  for time in strArr:
    times_l.append([turn_into_minutes(i) for i in time.split("-")])
  times_l.sort()
  most_free =  0
  for i in range(len(times_l)-1):
  	if times_l[i+1][0] - times_l[i][1] > most_free:
  		most_free =  times_l[i+1][0] - times_l[i][1]
  return "%02d:%02d" %(most_free/60, most_free%60) 

out=MostFreeTime(["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"])
print (out)



