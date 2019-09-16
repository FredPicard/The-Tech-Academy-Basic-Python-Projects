

import os
import time

path = r'C:\Users\Student\Documents\GitHub\The-Tech-Academy-Basic-Python-Projects\python_Drill.py'



file_List = os.listdir (path)
print("file_List", file_List)

for file in file_List:
   if file.endswith('.txt'):
      abPath = os.path.join(path, file)
      print(file)

      modification_time = os.path.getmtime(abPath)
      local_time = time.ctime(modification_time)
      print("Last modification time(Local Time)\\n:", local_time)



##for i in range(0,10):
##   abPath = os.path.join(path, file_List[i])
##   print(abPath)
