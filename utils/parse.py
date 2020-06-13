import pandas
import time as t
from utils import pub

def parsing(json_f):
    list = [x for x in json_f]
    mytopics = list[1:]
    time_d = {num: pandas.to_datetime(time, unit='ms').strftime("%d-%b-%y %H:%M:%S")
              for (num, time) in json_f.get("Timestamp").items()}
    for number in range(0, len(json_f['Timestamp'])):
        number = input("Gimme a number wrt to the timestamp: ")
        t.sleep(5)
        print(f"You chose {time_d[number]}")
        t.sleep(5)
        for top in range(0, len(mytopics)):
            topic = mytopics[top]
            value = json_f.get(topic).get(f"{number}")
            pub.publish(f"nou/{topic}", value)
