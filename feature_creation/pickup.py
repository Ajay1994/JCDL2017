op = open("pickup","wb")
count=0
with open("dumped_data_all_papers","rb") as infile:
	for line in infile:
		#print(line)
		#count+=1
		#if count==50:
		#	break
		if "#index" in line:
			op.write(str(line))
		elif "#@" in line:
			op.write(str(line))
		else:
			continue
op.close()
