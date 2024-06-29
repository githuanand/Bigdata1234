vcount = 0;  
ccount = 0;  
str = "Here is a string";  
   

str = str.lower();  
for i in range(0,len(str)):   
    
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1;
print("Given string:",str)
print("Total number of vowel and consonant are" );  
print(vcount);  
print(ccount); 
