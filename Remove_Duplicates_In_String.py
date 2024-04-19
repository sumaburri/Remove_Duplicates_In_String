string=input('Enter a String : ')
new_string=''
for ch in string:
    if ch not in new_string:
        new_string=new_string+ch
print(new_string)
