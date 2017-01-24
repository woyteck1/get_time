

import requests
import time

def Get_turnaround_time():
    """
    Queries the /status API endpoint and returns the current turnaround time and
    time stamp
    """
    r = requests.get('https://api.speechmatics.com/v1.0/status')
    status_json = r.json()
    return str(status_json['Time_UTC']), str(status_json['Average_Turnaround_Mins'])

def RUN():
    turnarounds = []
    times=[]
    for i in range(0,60):
      times.append(Get_turnaround_time()[0])
      turnarounds.append(Get_turnaround_time()[1])

      time.sleep(60)

    max_value = max(turnarounds)
    max_turnaround_time_element_index_for_use_in_finding_correct_time = int(turnarounds.index(max_value))
    print times[max_turnaround_time_element_index_for_use_in_finding_correct_time]

if __name__ == "__main__":
    RUN()






