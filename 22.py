
open_file = open("names.txt","r")
dic = open_file.read()
open_file.close()

dic = dic.replace('"','')
names = dic.split(",")
names.sort()

def letter_sc(char,):	
	letter_score =	 ord(char) - ord("A") + 1
	return letter_score

def  name_letter_sum(name):
	sum_letters_of_name = 0
	for e in name:
		sum_letters_of_name += letter_sc(e)
	return sum_letters_of_name

def  name_score(name,index):
	 alphabetical_value =  name_letter_sum(name) * (index + 1)
	 return alphabetical_value

def total_names(names):
	sum_of_values = 0
	for i in range(0,len(names)):
		sum_of_values += name_score(names[i],i)
	return sum_of_values

print total_names(names)


