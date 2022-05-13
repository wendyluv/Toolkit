'''
All functions and logic of the app must be defined here
*********************************************************
EDITED BY GWENDELINE OROZCO ON MAR 2 2022
CHANGES
ADDED THRUTH TABLE LOGIC
def __content_generator(string)
def __content_reformatter(content)
def __evaluator(inputs)
def __variables_columns_generator()
def __build_Table( Main_columns, inputs):
def generate_truth_table(expression)
*********************************************************
'''

from math import prod

TRUTH_TABLE_VARS = {}
KEYS=[]
ORIGINAL_EXPRESSION = None


#INTERNAL FUNCTION DONT USE
def __content_generator(string):
	global ORIGINAL_EXPRESSION 
	ORIGINAL_EXPRESSION = string
	content = []
	global TRUTH_TABLE_VARS
	global KEYS
	###ELIMINATES MULTICHARACTER OPERATIONS
	for i in range(2,len(string)):
		if(string[i-2]=="-" and string[i-1]==">"):
			if(content[-1]!=" is "):
				content.append("i");
			else:
				continue
		elif(string[i-2]=="<" and string[i-1]=="-" and string[i] == ">"):
			content.append(" is ");
		else:
			content.append(string[i-2])
	content.append(string[len(string)-2])
	content.append(string[len(string)-1])
	while(">"in content):
		content.remove(">")
		
	while("-"in content):
		content.remove("-")
	#SERACHES FOR ALL THE ACTIVE VARIABLES TU EVALUATE IN THE THRUTH TABLE
	for ltr in content:
		if ltr in['p','q','r','s','t','u','w','x','y','z']:
			TRUTH_TABLE_VARS[ltr] = False
	KEYS = list(TRUTH_TABLE_VARS.keys())
	return content



#INTERNAL FUNCTION DONT USE
def __content_reformatter(content):
	#TRANSLATES LOGICAL OPERATORS
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
	#TRANSLATES IMPLICATIONS AND EVALUATES MID-SIZE EXPRESSIONS
	for i in range(len(content)):
		if(content[i] == "i"):	
			content[0] = " (not  "+content[0]
			content[i-1] +=  " ) "
			content[i] = " or "
			try:		
				out.append(__evaluator("".join(content[0:i])))
				title.append("".join(content[0:i]))

				prev = i +1
			except:
				pass
		'''
		elif(content[i] == "d"):
			
			content[0]= "( not ( "+ content[0]
			content[i]= " "
			content[i-1]+= " ) or not ( "
			content[-1] += " ))"
			try:
				out.append(__evaluator("".join(content[0-1])))
				title.append("".join(content[0:-1]))
				prev = i +1
			except: pass
			#content[i-1], content[i], content[i+1] = " ( "+content[i-1]+ " and " + content [i+1]+" ) ", " or "," ( not "+content[i-1]+ " and not "  + content [i+1]+" )"			
		'''
	#EVALUATES LAST MID-SIZE EXPRESSION
	title.append("".join(content[prev:len(content)]))
	out.append(__evaluator("".join(content[prev:len(content)])))
	#EVALUATES THE WHOLE EXPRESSION
	final_expression = "".join(content)
	title.append(final_expression)
	out.append(__evaluator(final_expression))
	return title, out


#INTERNAL FUNCTION DONT USE
###EVALUATES AN (INPUT)STRING USING EVAL RETURNS A LIST WITH ALL CASES
def __evaluator(inputs):
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

#INTERNAL FUNCTION DONT USE	
def __variables_columns_generator():
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


#INTERNAL FUNCTION DONT USE, ASSEMBLES THE TABLE FROM MINOR ELEMENTS
def __build_Table( Main_columns, inputs):
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
'''
Recieves a logical expression, returns its truth table with the following format 
[
[HEADERS], 
[VALUES],
[VAlUES].
...
]
'''

def generate_truth_table(expression):
	global TRUTH_TABLE_VARS, KEYS, ORIGINAL_EXPRESSION
	TRUTH_TABLE_VARS = {}
	KEYS=[]
	ORIGINAL_EXPRESSION = None
	content = __content_generator(expression)
	inputs = __content_reformatter(content)
	Main_columns = __variables_columns_generator()
	table = __build_Table(Main_columns,inputs)
	return table





# ===================== Sets

def __get_union(set_a, set_b):
	output = set(set_a.copy())
	for elem in set_b:
		output.add(elem)
	
	return list(output)

def __get_difference(set_a, set_b):
	output = set(set_a.copy())

	for elem in set_b:
		if elem in output:
			output.remove(elem)
	
	return list(output)

def __get_intersection(set_a, set_b):
	output = set(set_a.copy())

	for elem in set_a:
		if elem not in set_b:
			output.remove(elem)
	
	return list(output)

def __get_symetric_difference(set_a, set_b):
	return __get_union(__get_difference(set_a, set_b), __get_difference(set_b, set_a))


def union(set_a, set_b, set_c):

	output = {}
	if set_a and set_b and set_c:
		output['A ∪ (B ∪ C)'] =  __get_union(__get_union(set_a, set_b), set_c)
	else:
		if set_a:
			if set_b:
				output['A ∪ B'] =  __get_union(set_a, set_b)
			elif set_c:
				output['A ∪ C'] =  __get_union(set_a, set_c)
		
		elif set_b:
			output['B ∪ C'] =  __get_union(set_a, set_c)
		
		else:
			# sets are incomplete
			return -1
	
	return output

def intersection(set_a, set_b, set_c):

	output = {}
	if set_a and set_b and set_c:
		output['A ∩ (B ∩ C)'] =  __get_intersection(__get_intersection(set_a, set_b), set_c)
	else:
		if set_a:
			if set_b:
				output['A ∩ B'] =  __get_intersection(set_a, set_b)
			elif set_c:
				output['A ∩ C'] =  __get_intersection(set_a, set_c)
		
		elif set_b:
			output['B ∩ C'] =  __get_intersection(set_a, set_c)
		
		else:
			# sets are incomplete
			return -1
	
	return output

def difference(set_a, set_b, set_c):
	
	output = {}

	if set_a:
		# difference between set b and set c
		if set_c:
			output["A - C"] = __get_difference(set_a, set_c)
		if set_b:
			output["A - B"] = __get_difference(set_a, set_b)
	elif set_b:
		# difference between set a and set c
		if set_a:
			output["A - B"] = __get_difference(set_a, set_b)
		if set_c:
			output["B - C"] = __get_difference(set_b, set_c)
	if set_c:
		# difference between set a and set b
		if set_a:
			output["A - C"] = __get_difference(set_a, set_c)
		if set_b:
			output["B - C"] = __get_difference(set_b, set_c)
	
	return output

def symetric_difference(set_a, set_b, set_c):

	output = {}


	if set_a:
		# difference between set b and set c
		if set_c:
			output["A Δ C"] = __get_symetric_difference(set_a, set_c)
		if set_b:
			output["A Δ B"] = __get_symetric_difference(set_a, set_b)
	elif set_b:
		# difference between set a and set c
		if set_a:
			output["A Δ B"] = __get_symetric_difference(set_a, set_b)
		if set_c:
			output["B Δ C"] = __get_symetric_difference(set_b, set_c)
	if set_c:
		# difference between set a and set b
		if set_a:
			output["A Δ C"] = __get_symetric_difference(set_a, set_c)
		if set_b:
			output["B Δ C"] = __get_symetric_difference(set_b, set_c)
	
	return output


# ====== Relations and Functions

def convert_string_to_set(string):
	"""
	Converts a string of tuples into a set
	"""
	if " " in string: # cannot have whitespaces
		return False

	list_tuples = string.split('),')
	new_set = set()
	for elem in list_tuples:
		elem_a, elem_b = elem.split(',')
		elem_a = elem_a[1:]
		if ')' in elem_b:
			elem_b = elem_b[:-1]
		
		new_set.add((int(elem_a), int(elem_b)))
	
	return new_set


def convert_single_string_to_set(string):
	"""
	Converts a string of tuples into a set
	"""
	if " " in string: # cannot have whitespaces
		return False

	new_set = set()
	for elem in string:
		if elem == " " or elem == ",": 
			continue
		
		new_set.add(int(elem))

	return new_set



def is_symetric(set_a, set_pairs): # will receive a set of tuples
	"""
	Propiedad simétrica
	La propiedad simétrica establece que para todos los números reales x y y ,
	si x = y , entonces y = x .
	"""
	for elem in set_pairs:
		lst_elem = list(elem)
		if (lst_elem[1], lst_elem[0]) not in set_a:
			return False

	return True

def is_reflexive(set_a, set_pairs):
	"""
	Propieda reflexiva
	La propiedad reflexiva establece que para cada número real x , x = x .
	"""
	for elem in set_a:
		if (elem, elem) not in set_pairs:
			return False

	return True


def is_transitive(set_a, set_pairs):
	"""
	Propiedad transitiva
	La propiedad transitiva establece que para todos los números reales x , y , y z ,
	si x = y y y = z , entonces x = z .
	"""
	for elems in set_pairs:
		pair = list(elems)
		for elem in set_a:
			if (pair[1], elem) in set_pairs: # transitividad
				return True

	return False

def domAndCo(relation_set):
	domain = set()
	codom = set()
	for elem in relation_set:
		domain.add(elem[0])
		codom.add(elem[1])
	
	return "Domain: " + "".join(list( str(e) for e in domain)) + "\n" +  "Codomain: " + "".join(list( str(f) for f in codom)) + "\n"

def is_function(relation_set):
	hashed = {}
	for elem in relation_set:
		if(hashed.get(elem[0], False)):
			return False
		else:
			hashed[elem[0]] = True 
	return True
# Entrega parcial Series y sucesiones	
	
def series(s, inf, sup):
	a = [] 
	rec(s, inf, sup,a)
	s = sum(a)
	p = prod(a)
	a.append(s)
	a.append(p)
	
	return a

def rec(s, inf, sup, a):
	if inf <=  sup:
		k= inf
		a.append((eval(s)))
		rec(s, inf+1, sup,a)
 
if __name__ == "__main__":
	while(True):
		inf = int(input("Ingresa Limite inferior: "))
		sup = int(input("Ingresa Limite superior: "))
		eq = input("Formula(k): ")
		serie = series(eq,inf,sup)
		
		print("n-esimo termino de la serie")
		for i in range(len(serie)): 
			print(i,": ",serie[i],sep="")
		print("Sumatoria: ", sum(serie))
		
		print("multiplicativo: ", prod(serie))
		try:
			if not(int(input("Ingrese 0 y enter para salir.\n"))):
				break	
		except Exception:
			pass
