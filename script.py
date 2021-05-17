import sys
import random
import json

print(sys.version)
print(sys.executable)

nums = []

for x in range(1000):
  nums.append(random.randint(1,100)) 




json.dump(nums, open('data.json', 'w') )