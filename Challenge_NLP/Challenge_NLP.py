#!/usr/bin/env python
# coding: utf-8

# # NAME :- MOHAN SAI KOTHAPALLI
# # EMP ID :- 2112951
# # COHORT CODE :- GN22CDBDS001

# ## ASSIGNMENT ON REGEX

# Design a python program to accept a file name through command line arguments.
# 
# Parse this file to perform the following:
# 
# 1. Print all currencies in text, Accepted- $, ₹, £ 
# 
# 2. Print all date times in the text- dd/mm/yyyy, dd/mm/yy, mm/dd/yyyy, mm/dd/yy
# 
# 3. Print all cardinilities and orders- 4th, fifth, sixth, 1st, 2nd, nineteenth, fifth
# 
# 4. Print all 4 letter words that begin with vowels

# ### STEP 0 :- IMPORTING LIBRARIES

# In[109]:


import re
import sys


# # DATA 1
# ### STEP 1 :- Opening File DATA 1
# #### This file contains some random text with currency's  and dates and some orders.

# In[110]:


f=open(sys.argv[1])


# In[111]:


with open(sys.argv[1],'r',encoding='utf-8') as f:
    data=f.readline()
data


# ## The above 'readline()' will read a single line from the file. Line means when you press "enter" in the keyboard will typing your data that is considered as new line. Without pressing you keep on typing then it is considered as single line. i.e '\n'

# In[112]:


with open(sys.argv[1],'r',encoding='utf-8') as f:
    data=f.readlines()
data


# ## The above 'readlines()' will read all lines from the file as list. Each line as an element in list.

# In[113]:


with open(sys.argv[1],'r',encoding='utf-8') as f:
    data=f.read()
data


# ## The above 'read()' will read all lines from the file as single para.

# ### STEP 2:- FINDING CURRENCY'S INCLUDING THE AMOUNT IN TEXT

# In[114]:


x=re.findall(r"(\d*?\.?\d+ ?[$₹£])",data)


# In[115]:


print(x)


# ### FINDING ONLY THE SYMBOLS OF CURRENCY IN TEXT

# In[116]:


curr=re.findall("([$₹£])",data)


# In[117]:


print("Total Number Of Currency Symbols In the TEXT DATA are : ",len(curr))
print(f"Types Of Currency Symbols In the TEXT DATA are : ",len(set(curr))," ",set(curr))
print(curr)


# ### STEP 3 :-PRINTING ALL THE FORMATES OF DATES IN THE TEXT 

# In[118]:


dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b)",data)
print("The Number of dates in the format of 'mm/dd/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b)",data)
print("The Number of dates in the format of 'dd/mm/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})\b)",data)
print("The Number of dates in the format of 'dd/mm/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})\b)",data)
print("The Number of dates in the format of 'mm/dd/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()


# ### STEP 4 :-  PRINTING ALL CARDINILITIES AND ORDERS FROM THE TEXT

# In[119]:


order=[]
x=re.findall(r"((first|second|third|sixth)|(thir[a-z]+(th|st|nd))|(fou[a-z]+(th|rd|st|nd))|(fif[a-z]+(th|st|nd|rd))|(fi[a-z]+th)|(six[a-z]+(th|st|nd|rd))|(sev[a-z]+(th|st|nd|rd))|(eig[a-z]+(th|st|nd|rd))|(nine[a-z]+(th|st|nd|rd))|(ten[a-z]+?(th|st|nd|rd))|(ele[a-z]+th)|(twe[a-z]+(th|st|nd|rd))|(hun[a-z]+(th|st|rd)))",data)
for i in range(len(x)):
    if(x[i][0] not in order):
        order.append(x[i][0])
#print(order)
orders=[]
x1=re.findall(r"([0-9]+(th|st|nd|rd))",data)
for i in range(len(x1)):
    if(x1[i][0] not in orders):
        orders.append(x1[i][0])
#print(orders)
if order or orders:
    print(order+orders)
else:
    print("No CARDINILITIES AND ORDERS FOUND IN THE TEXT")


# ### STEP 5 :- PRINTING ALL 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT 

# In[120]:


four=re.findall(r"(\b(a|e|i|o|u|A|E|I|O|U)[a-zA-Z]{3}\b)",data)
fours=[]
for i in range(len(four)):
    fours.append(four[i][0])
print(fours)


# ## WE WILL REPEAT THE ABOVE STEPS FOR THE REMAINING DATASETS

# # DATA 2

# ### STEP 1 :- Opening File DATA 2
# #### This TEXT file contains a story and some values of currency's.

# In[121]:


f=open(sys.argv[2])


# In[122]:


with open(sys.argv[2],'r',encoding='utf-8') as f:
    data=f.readline()
data


# In[123]:


with open(sys.argv[2],'r',encoding='utf-8') as f:
    data=f.readlines()
data


# In[124]:


with open(sys.argv[2],'r',encoding='utf-8') as f:
    data=f.read()
data


# ### STEP 2:- FINDING CURRENCY'S INCLUDING THE AMOUNT IN TEXT

# In[125]:


x=re.findall(r"(\d*?\.?\d+ ?[$₹£])",data)


# In[126]:


x


# ### FINDING ONLY THE SYMBOLS OF CURRENCY IN TEXT

# In[127]:


curr=re.findall("([$₹£])",data)


# In[128]:


print("Total Number Of Currency Symbols In the TEXT DATA are : ",len(curr))
print(f"Types Of Currency Symbols In the TEXT DATA are : ",len(set(curr))," ",set(curr))
print(curr)


# ### STEP 3 :-PRINTING ALL THE FORMATES OF DATES IN THE TEXT 

# In[129]:


dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b)",data)
print("The Number of dates in the format of 'mm/dd/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b)",data)
print("The Number of dates in the format of 'dd/mm/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})\b)",data)
print("The Number of dates in the format of 'dd/mm/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})\b)",data)
print("The Number of dates in the format of 'mm/dd/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()


# ### STEP 4 :-  PRINTING ALL CARDINILITIES AND ORDERS FROM THE TEXT

# In[130]:


order=[]
x=re.findall(r"((first|second|third|sixth)|(thir[a-z]+(th|st|nd))|(fou[a-z]+(th|rd|st|nd))|(fif[a-z]+(th|st|nd|rd))|(fi[a-z]+th)|(six[a-z]+(th|st|nd|rd))|(sev[a-z]+(th|st|nd|rd))|(eig[a-z]+(th|st|nd|rd))|(nine[a-z]+(th|st|nd|rd))|(ten[a-z]+?(th|st|nd|rd))|(ele[a-z]+th)|(twe[a-z]+(th|st|nd|rd))|(hun[a-z]+(th|st|rd)))",data)
for i in range(len(x)):
    if(x[i][0] not in order):
        order.append(x[i][0])
#print(order)
orders=[]
x1=re.findall(r"([0-9]+(th|st|nd|rd))",data)
for i in range(len(x1)):
    if(x1[i][0] not in orders):
        orders.append(x1[i][0])
#print(orders)
if order or orders:
    print(order+orders)
else:
    print("No CARDINILITIES AND ORDERS FOUND IN THE TEXT")


# ### STEP 5 :- PRINTING ALL 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT 

# In[131]:


four=re.findall(r"(\b(a|e|i|o|u|A|E|I|O|U)[a-zA-Z]{3}\b)",data)
fours=[]
for i in range(len(four)):
    fours.append(four[i][0])
print(fours)


# # DATA 3

# ### STEP 1 :- Opening File DATA 3
# #### This TEXT file contains INDIAN CONSTUITIONAL AMENDAMENTS with dates and order of the AMENDEMETS.
# #### As there are no currencys in this file i have included some random currency symbols with and without amounts (4)

# In[132]:


f=open(sys.argv[3])


# In[133]:


with open(sys.argv[3],'r',encoding='utf-8') as f:
    data=f.readline()
data


# In[134]:


with open(sys.argv[3],'r',encoding='utf-8') as f:
    data=f.readlines()
data


# In[135]:


with open(sys.argv[3],'r',encoding='utf-8') as f:
    data=f.read()
data


# ### STEP 2:- FINDING CURRENCY'S INCLUDING THE AMOUNT IN TEXT

# In[136]:


x=re.findall(r"(\d*?\.?\d+ ?[$₹£])",data)


# In[137]:


x


# ### FINDING ONLY THE SYMBOLS OF CURRENCY IN TEXT

# In[138]:


curr=re.findall("([$₹£])",data)


# In[139]:


print("Total Number Of Currency Symbols In the TEXT DATA are : ",len(curr))
print(f"Types Of Currency Symbols In the TEXT DATA are : ",len(set(curr))," ",set(curr))
print(curr)


# ### STEP 3 :-PRINTING ALL THE FORMATES OF DATES IN THE TEXT 

# In[140]:


dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b)",data)
print("The Number of dates in the format of 'mm/dd/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b)",data)
print("The Number of dates in the format of 'dd/mm/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})\b)",data)
print("The Number of dates in the format of 'dd/mm/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})\b)",data)
print("The Number of dates in the format of 'mm/dd/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()


# ### STEP 4 :-  PRINTING ALL CARDINILITIES AND ORDERS FROM THE TEXT

# In[141]:


order=[]
x=re.findall(r"((first|second|third|sixth)|(thir[a-z]+(th|st|nd))|(fou[a-z]+(th|rd|st|nd))|(fif[a-z]+(th|st|nd|rd))|(fi[a-z]+th)|(six[a-z]+(th|st|nd|rd))|(sev[a-z]+(th|st|nd|rd))|(eig[a-z]+(th|st|nd|rd))|(nine[a-z]+(th|st|nd|rd))|(ten[a-z]+?(th|st|nd|rd))|(ele[a-z]+th)|(twe[a-z]+(th|st|nd|rd))|(hun[a-z]+(th|st|rd)))",data)
for i in range(len(x)):
    if(x[i][0] not in order):
        order.append(x[i][0])
#print(order)
orders=[]
x1=re.findall(r"([0-9]+(th|st|nd|rd))",data)
for i in range(len(x1)):
    if(x1[i][0] not in orders):
        orders.append(x1[i][0])
#print(orders)
if order or orders:
    print(order+orders)
else:
    print("No CARDINILITIES AND ORDERS FOUND IN THE TEXT")


# ### STEP 5 :- PRINTING ALL 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT 

# In[142]:


four=re.findall(r"(\b(a|e|i|o|u|A|E|I|O|U)[a-zA-Z]{3}\b)",data)
fours=[]
for i in range(len(four)):
    fours.append(four[i][0])
print(fours)
print("Tolal number of words without repetition are : ",len(set(fours)),"\n",set(fours))


# # DATA 4

# ### STEP 1 :- Opening File DATA 4
# #### This TEXT file contains fluctuation of indian currency with dollar and pound daywise.

# In[143]:


f=open(sys.argv[4])


# In[144]:


with open(sys.argv[4],'r',encoding='utf-8') as f:
    data=f.readline()
data


# In[145]:


with open(sys.argv[4],'r',encoding='utf-8') as f:
    data=f.readlines()
data


# In[146]:


with open(sys.argv[4],'r',encoding='utf-8') as f:
    data=f.read()
data


# ### STEP 2:- FINDING CURRENCY'S INCLUDING THE AMOUNT IN TEXT

# In[147]:


x=re.findall(r"(\d*\.?\d+ ?[$₹£])",data)
x1=re.findall(r"([$₹£] ?\d*\.?\d+)",data)


# In[148]:


print(x+x1)


# ### FINDING ONLY THE SYMBOLS OF CURRENCY IN TEXT

# In[149]:


curr=re.findall("([$₹£])",data)


# In[150]:


print("Total Number Of Currency Symbols In the TEXT DATA are : ",len(curr))
print(f"Types Of Currency Symbols In the TEXT DATA are : ",len(set(curr))," ",set(curr))


# ### STEP 3 :-PRINTING ALL THE FORMATES OF DATES IN THE TEXT 

# In[151]:


dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b)",data)
print("The Number of dates in the format of 'mm/dd/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b)",data)
print("The Number of dates in the format of 'dd/mm/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})\b)",data)
print("The Number of dates in the format of 'dd/mm/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})\b)",data)
print("The Number of dates in the format of 'mm/dd/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()


# ### STEP 4 :-  PRINTING ALL CARDINILITIES AND ORDERS FROM THE TEXT

# In[152]:


order=[]
x=re.findall(r"((first|second|third|sixth)|(thir[a-z]+(th|st|nd))|(fou[a-z]+(th|rd|st|nd))|(fif[a-z]+(th|st|nd|rd))|(fi[a-z]+th)|(six[a-z]+(th|st|nd|rd))|(sev[a-z]+(th|st|nd|rd))|(eig[a-z]+(th|st|nd|rd))|(nine[a-z]+(th|st|nd|rd))|(ten[a-z]+?(th|st|nd|rd))|(ele[a-z]+th)|(twe[a-z]+(th|st|nd|rd))|(hun[a-z]+(th|st|rd)))",data)
for i in range(len(x)):
    if(x[i][0] not in order):
        order.append(x[i][0])
#print(order)
orders=[]
x1=re.findall(r"([0-9]+(th|st|nd|rd))",data)
for i in range(len(x1)):
    if(x1[i][0] not in orders):
        orders.append(x1[i][0])
#print(orders)
if order or orders:
    print(order+orders)
else:
    print("No CARDINILITIES AND ORDERS FOUND IN THE TEXT")


# ### STEP 5 :- PRINTING ALL 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT 

# In[153]:


four=re.findall(r"(\b(a|e|i|o|u|A|E|I|O|U)[a-zA-Z]{3}\b)",data)
fours=[]
if four:
    for i in range(len(four)):
        fours.append(four[i][0])
    print(fours)
    print("Tolal number of words without repetition are : ",len(set(fours)),"\n",set(fours))
else:
    print("NO 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT")


# # DATA 5

# ### STEP 1 :- Opening File DATA 5
# #### This TEXT file contains a book about indian history.

# In[154]:


f=open(sys.argv[5])


# In[155]:


with open(sys.argv[5],'r',encoding='utf-8') as f:
    data=f.read()
data


# ### STEP 2:- FINDING CURRENCY'S INCLUDING THE AMOUNT IN TEXT

# In[156]:


x=re.findall(r"(\d*\.?\d+ ?[$₹£])",data)
x1=re.findall(r"([$₹£] ?\d*\.?\d+)",data)


# In[157]:


print(x+x1)


# ### STEP 3 :-PRINTING ALL THE FORMATES OF DATES IN THE TEXT 

# In[158]:


dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b)",data)
print("The Number of dates in the format of 'mm/dd/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b)",data)
print("The Number of dates in the format of 'dd/mm/yyyy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})\b)",data)
print("The Number of dates in the format of 'dd/mm/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()
dates=re.findall(r"((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})\b)",data)
print("The Number of dates in the format of 'mm/dd/yy' are : ",len(dates))
for i in range(len(dates)):
    print(dates[i][0],end='  ')
print()


# ### STEP 4 :-  PRINTING ALL CARDINILITIES AND ORDERS FROM THE TEXT

# In[159]:


order=[]
x=re.findall(r"((first|second|third|sixth)|(thir[a-z]+(th|st|nd))|(fou[a-z]+(th|rd|st|nd))|(fif[a-z]+(th|st|nd|rd))|(fi[a-z]+th)|(six[a-z]+(th|st|nd|rd))|(sev[a-z]+(th|st|nd|rd))|(eig[a-z]+(th|st|nd|rd))|(nine[a-z]+(th|st|nd|rd))|(ten[a-z]+?(th|st|nd|rd))|(ele[a-z]+th)|(twe[a-z]+(th|st|nd|rd))|(hun[a-z]+(th|st|rd)))",data)
for i in range(len(x)):
    if(x[i][0] not in order):
        order.append(x[i][0])
#print(order)
orders=[]
x1=re.findall(r"([0-9]+(th|st|nd|rd))",data)
for i in range(len(x1)):
    if(x1[i][0] not in orders):
        orders.append(x1[i][0])
#print(orders)
if order or orders:
    print(order+orders)
else:
    print("No CARDINILITIES AND ORDERS FOUND IN THE TEXT")


# ### STEP 5 :- PRINTING ALL 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT 

# In[160]:


four=re.findall(r"(\b(a|e|i|o|u|A|E|I|O|U)[a-zA-Z]{3}\b)",data)
fours=[]
if four:
    for i in range(len(four)):
        fours.append(four[i][0])
    print("Tolal number of words without repetition are : ",len(set(fours)),"\n",set(fours))
else:
    print("NO 4 LETTER WORDS STARTING WITH VOWELS FROM THE TEXT")


# In[ ]:





# In[ ]:




