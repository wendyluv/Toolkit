"""
All functions and logic of the app must be defined here
"""
content_generator(string):
	content = []
	for i in range(2,len(string)):
		if(string[i-2]="-" and string[i-1]=">"):
			content.append("i");
		elif(string[i-2]="<" and string[i-1]="-" and string[i] == ">"):
			content.append("d");
		else:
			content.append(string[i-2])
	content.append(string[-2])
	content.append(string[-1])
	return content

content_reformatter(content):
	for i in range(len(string)):
		if(content[i] == "^"):
			content[i] = " or "
		elif(content[i] == "v"):
			content[i] = " and "
		elif(content[i] == "~"):
			content[i] = " not "
		else:
			pass
	for i in range(len(string)):
		if(content[i] == "i"):
			content [0] = " not ( "+content[0]
			content [i-1] +=  " ) "
			content [i] = " or "
		elif(content[i] == "d"):
			content[i-1], content[i], content[i+1] = " ( "+content[i-1]+ " and " + content [i+1]+" ) ", " or ", ( not "+content[i-1]+ " and not "  + content [i+1]+" ) "			
		else: pass
		return "".join(content)

truth_table_generator(input):
	p = 0
	q = 0
	r = 0
	s = 0
	t = 0
	
	results = []
	for i in range(32):
		results.append(eval(input))
		if (t == 0):
			t++
		else:
			t--
		if (i%2):
			if (s == 0):
				s++
			else:
				s--
			if(i%4):
				if (r == 0):
					r++
				else:
					r--
				if(i%8):
					if (q == 0):
						q++
					else:
						q--
					if(i%16):
						if(p == 0):
							p++
						else:
							p--
	return results
	
