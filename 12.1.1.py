n=int(input())
ph = {}
for i in range (n):
	CMD = input().split()
	if CMD[0] == "ADD":
		ph[CMD[1]] = CMD[2]
	elif CMD[0]=="REMOVE":
		ph.pop(CMD[1],None)
	elif CMD[0]=="DISPLAY":
		if len(ph) == 0:
			print("No contacts")
		else:
			for name in sorted(ph):
				print(f"{name}: {ph[name]}")
