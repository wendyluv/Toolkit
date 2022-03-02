"""
All functions and logic of the app must be defined here
"""
TRUTH_TABLE_VARS = {}
KEYS=[]
ORIGINAL_EXPRESSION = None
def content_generator(string):
	global ORIGINAL_EXPRESSION 
	ORIGINAL_EXPRESSION = string
	content = []
	global TRUTH_TABLE_VARS
	global KEYS
	for i in range(2,len(string)):
		if(string[i-2]=="-" and string[i-1]==">"):
			if(content[-1]!="d"):
				content.append("i");
			else:
				continue
		elif(string[i-2]=="<" and string[i-1]=="-" and string[i] == ">"):
			content.append("d");
		else:
			content.append(string[i-2])
	content.append(string[len(string)-2])
	content.append(string[len(string)-1])
	while(">"in content):
		content.remove(">")
	for ltr in content:
		if ltr in['p','q','r','s','t']:
			TRUTH_TABLE_VARS[ltr] = False
	KEYS = list(TRUTH_TABLE_VARS.keys())
	return content

def content_reformatter(content):
	for i in range(len(content)):
		if(content[i] == "^"):
			content[i] = " and "
		elif(content[i] == "v"):
			content[i] = " or "
		elif(content[i] == "~"):
			content[i] = " not "
		else:
			pass
	early_outputs = []
	out = []
	title = []
	prev = 0
	for i in range(len(content)):
		if(content[i] == "i"):	
			title.append("".join(content[prev:i]))
			out.append(evaluator("".join(content[prev:i])))
			prev = i+1 	
			content[0] = " not(  "+content[0]
			content[i-1] +=  " ) "
			content[i] = " or "
			
		elif(content[i] == "d"):
			title.append("".join(content[prev:i]))
			out.append(evaluator("".join(content[prev:i])))
			prev = i+1
			content[i-1], content[i], content[i+1] = " ( "+content[i-1]+ " and " + content [i+1]+" ) ", " or "," ( not "+content[i-1]+ " and not "  + content [i+1]+" )"			
		else: pass
	title.append("".join(content[prev:len(content)]))
	out.append(evaluator("".join(content[prev:len(content)])))
	final_expression = "".join(content)
	title.append(final_expression)
	out.append(evaluator(final_expression))
	return title, out



def evaluator(inputs):
	global TRUTH_TABLE_VARS
	global KEYS
	for k in KEYS:
		TRUTH_TABLE_VARS[k] =False
	results = []
	for i in range(1,1+2**len(KEYS)):
		results.append(eval(inputs,TRUTH_TABLE_VARS))
		divisor = 1
		index = len(KEYS) 
		while(i%divisor == 0):
			divisor *=2
			index -= 1
			key = KEYS[index]
			TRUTH_TABLE_VARS[key] = not TRUTH_TABLE_VARS[key]
		
	return results
	
def variables_columns_generator():
	global TRUTH_TABLE_VARS
	global KEYS
	for k in KEYS:
		TRUTH_TABLE_VARS[k] =False
	values = []
	for i in range(1,1+2**len(KEYS)):
		values.append([])
		for k in KEYS:
			values[-1].append(TRUTH_TABLE_VARS[k])
		divisor = 1
		index = len(KEYS) 
		while(i%divisor == 0):
			divisor *=2
			index -= 1
			key = KEYS[index]
			TRUTH_TABLE_VARS[key] = not TRUTH_TABLE_VARS[key]
	return values

def build_Table( Main_columns, inputs):
	table = KEYS[:]
	titles, results = inputs
	titles[-1] = ORIGINAL_EXPRESSION
	table += titles
	transposed_results = [[results[j][i] for j in range(len(results))] for i in range(len(results[0]))]
	for i in range(len(Main_columns)):
		Main_columns[i] += transposed_results[i]
	table = [table]	
	table+= Main_columns
	
	return table


if __name__ == "__main__":
	string = input()
	content = content_generator(string)
	inputs = content_reformatter(content)
	Main_columns = variables_columns_generator()
	table = build_Table(Main_columns,inputs) 
	for row in table:
		print(row)
