name=input()

result=name.split(" ")

l=len(result)

if(l>2):
	output=result[l-1]+", "+result[0][:1]+"."+result[l-2][:1]+"."
else:
	output=result[l-1]+", "+result[0][:1]+"."

print(output)