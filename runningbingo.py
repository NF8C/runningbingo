import random

counts = []

def makelist():
  q=0
  list = []
  while q < 60:
	  list.append(q)
	  q+=1	
  return list

def simulate():
  lists = makelist()
  trys = 0
  while len(lists) > 0: 
  	r = random.randint(0,59)
  	if r in lists:
	  	lists.remove(r)
  	trys += 1
  return trys
  	
d = simulate()

x=0
simulations = []
while x < 1000:
	simulations.append(simulate())
	trys = sum(simulations)
	x+=1
	trys = trys/x

print(trys)



	
