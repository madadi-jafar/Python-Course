full_name = input("Enter your full name: ").strip()
#in here we change the name in to title case
#in here we use len meathod to compute the length of the string 
#and also we use the replase meathod to remove the spaces between the word 
print("The length with no space is",len(full_name.replace(" ","")))
#we use [:: -1] to revers the string
print(full_name[::-1])
