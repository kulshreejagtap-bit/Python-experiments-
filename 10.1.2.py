def reverse_string(str1):
	result=""
	ln=len(str1)
	for i in range(ln-1,-1,-1):
		result=result+str1[i]
	return result
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
