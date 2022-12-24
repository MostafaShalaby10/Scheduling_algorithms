import numpy as np
from operator import itemgetter
# times = [
#     [10, 20, 120, 'A'], [20, 20, 20 , 'B'], [40, 20, 50 , "C"], [50, 20, 90 , "D"], [60, 20, 70 , "E"] ,[100 , 20 , 110 , "F"]
# ]
# times = sorted(times , key=itemgetter(2))
# print(times)
# # # ----------------------FCFS-----------------------------------# #
# print("Task no : ",times[0][3]," isn't Missed" )
# sum = times[0][0] + times[0][1]
# print("Started from " , times[0][0] , " TO " , sum)
# for i in range(1, len(times)):
#     if (sum > times[i][2]):
#         print("Task no : ", times[i][3], " is Missed")
#     elif(sum > times[i][0]):
#         sum = sum + times[i][1]
#         print("Task no : ", times[i][3], " isn't Missed")
#         print("Started from ", (sum - int(times[i][1])), " TO ", sum)
#
#     else:
#         sum = sum + times[i][1] + (times[i][0] - sum)
#         print("Task no : ", times[i][3], " isn't Missed")
#         print("Started from ", (sum - int(times[i][1])), " TO ", sum)