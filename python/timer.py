# This script runs the specified python script and returns its runtime

file = str(input("What file would you like to test (include extension)?  "))
file = file.join(file.split()).lower()

import time, os

try:
    start = time.time()
    os.system(f'python3 {file}')
except:
    print(f"Error: The file '{file}' does not exist")

print((str(file) + "\'s Runtime: %s Seconds" % (time.time() - start)))

