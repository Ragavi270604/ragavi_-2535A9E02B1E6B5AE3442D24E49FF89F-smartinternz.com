import pandas as pd

def mean(arr):
  return sum(arr) / len(arr)

def isEven (arr):
  return arr % 2 == 0

def half (arr):
  if isEven(len(arr)):
    return int(len(arr)/2) - 1
  else:
    return int(len(arr)/2)

def median (arr):
    sortedList = sorted(arr)
    index = half(sortedList)
    if isEven(len(sortedList)):
        return mean([ sortedList[index], sortedList[index + 1] ])
    else:
        return sortedList[index]

data = [
  {"name": "John",  "distance": 5602,  "high-speed-running": 504},
  {"name": "Mike",  "distance": 5242,  "high-speed-running": 622},
  {"name": "Chad",  "distance": 4825,  "high-speed-running": 453},
  {"name": "Phil",  "distance": 611,   "high-speed-running": 500},
  {"name": "Tyler", "distance": 5436,  "high-speed-running": 409}
]

df = pd.DataFrame(data)