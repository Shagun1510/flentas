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
