  
import re 

def change_case(input_st): 
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_st) 
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower() 
	
# Driver code 
input_st = "My Name is Bashir123"
print(change_case(input_st)) 






 
input_st = 'My Name Is Bashir 123'

# printing original string 
print("The original string is : " + input_st) 

# Convert Snake case to Pascal case 
# Using title() + replace() 
lw = input_st.replace("_", " ").lower().replace(" ", "") 
up = input_st.replace("_", " ").upper().replace(" ", "") 
tit = input_st.replace("_", " ").title().replace(" ", "") 
# printing result 
print("The String after changing case : " + str(lw)) 
print("The String after changing case : " + str(up))
print("The String after changing case : " + str(tit))

