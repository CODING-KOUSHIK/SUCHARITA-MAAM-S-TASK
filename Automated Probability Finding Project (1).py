#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df=pd.read_excel("Book1.xlsx")


# In[ ]:


df


# In[ ]:


df.columns


# In[ ]:


num_column=[]
for i in range(df.shape[1]):
    if df[df.columns[i]].dtypes!='O':
        num_column.append(df.columns[i])
        
        
num_column


# In[ ]:


sum(df.loc[0,num_column])


# In[ ]:


list1=[]
for i in range(df.shape[0]):
    list1.append(sum(df.loc[i,num_column]))
df['total']=list1
df


# In[ ]:





# In[ ]:


dict1={df.columns[0]:'total'}
for i in range(1,df.shape[1]):
    dict1[df.columns[i]]=df[df.columns[i]].sum()
    

df = df.append(dict1, ignore_index = True)
dict1


# In[ ]:


df


# In[ ]:


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# In[ ]:


c_list=['BLUE','PURPLE','CYAN','DARKCYAN','GREEN','YELLOW','RED']


# In[39]:


while True:
    print(color.UNDERLINE + "Read the Instruction before enter a input" + color.END)
    print('\n'*1)
    print(color.DARKCYAN + color.BOLD +'For UNION Press 1' + color.END, ) 
    print(color.PURPLE + color.BOLD +'For INTERSECTION Press 2' + color.END, ) 
    print(color.CYAN + color.BOLD +'For PROBABILITY MATRIX Press 3' + color.END, )
    print(color.RED + color.BOLD +'For EXIT Press 4' + color.END, )
    
    print('\n'*1)
    x1=input("Your input = ")
    
    print(color.GREEN + color.BOLD +'For Intersection you have to choose two data' + color.END)
    print('\n'*1)
    if x1=='1' or x1=='2':
        for i in range(0,df.shape[0]-1):
            print(f"{getattr(color, c_list[i]) + color.BOLD} for {df.loc[i,df.columns[0]]} press: {i}")

        x2=int(input("Your input = "))
        print('\n'*1)


        if x2 in range(0,df.shape[0]-1):
            for i in range(1,df.shape[1]-1):
                print(f"{getattr(color, c_list[i]) + color.BOLD} for {df.columns[i]} press: {i}")

            x3=int(input("Your input = "))
            if x3 in range(1,df.shape[1]-1):
                x4=df.columns[x3]


                if x1=='1':
                    op=df.loc[df.shape[0]-1,x4] + df.loc[x2,df.columns[df.shape[1]-1]] - df.loc[x2,x4]
                    total=df.loc[df.shape[0]-1,df.columns[df.shape[1]-1]]
                    print(f"{color.BLUE + color.UNDERLINE} From the given data Union of {df.loc[x2,df.columns[0]]} and {df.columns[x3]} is {color.END} {color.BOLD + color.RED}{round(op/total,4)}{color.END}")
                    print("#"*70)
                    print('\n'*2)

                elif x1=='2':
                    op=df.loc[x2,x4]
                    total=df.loc[df.shape[0]-1,df.columns[df.shape[1]-1]]
                    print(f"{color.BLUE + color.UNDERLINE} From the given data Intersection of {df.loc[x2,df.columns[0]]} and {df.columns[x3]} is {color.END} {color.BOLD + color.RED}{round(op/total,4)}{color.END}")
                    print("#"*70)
                    print('\n'*2)



            else:
                print(color.RED + color.BOLD +'MAY BE SOME INVALIED INPUT' + color.END,)
        else:
            print(color.RED + color.BOLD +'MAY BE SOME INVALIED INPUT' + color.END,)
    elif x1=='3':
        pro_df=df.copy()
        num_column=[]
        for i in range(df.shape[1]):
            if df[df.columns[i]].dtypes!='O':
                num_column.append(df.columns[i])
        for col in num_column:
            total=df.loc[df.shape[0]-1,df.columns[df.shape[1]-1]]
            pro_df[col]=df[col]/total
        formatted_pro_df = pro_df.to_string(index=False)  # Convert DataFrame to string

        print(color.DARKCYAN + color.BOLD + formatted_pro_df + color.END)
        print('\n' * 2)
        
    
    elif x1=='4':
        print(color.GREEN + color.BOLD +'I THINK YOU GOT YOUR ANSWER' + color.END,)
        print(color.GREEN + color.BOLD +'THANK YOU FOR CHECKING THIS CODE' + color.END,)
        print('\n'*2)
        break

    else:
        print(color.RED + color.BOLD +'MAY BE SOME INVALIED INPUT' + color.END,)
        print('\n'*2)

                  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


while True:
    print(color.UNDERLINE + "Read the Instruction before entering input" + color.END)
    print('\n' * 1)
    print(color.DARKCYAN + color.BOLD + 'For UNION Press 1' + color.END)
    print(color.PURPLE + color.BOLD + 'For INTERSECTION Press 2' + color.END)
    print(color.RED + color.BOLD + 'For EXIT Press 3' + color.END)
    print('\n' * 1)
    x1 = input("Your input = ")

    def print_data_options():
        for i in range(df.shape[0]):
            print(f"for {df.loc[i, df.columns[0]]} press: {i}")

    if x1 == '1' or x1 == '2':
        print(color.GREEN + color.BOLD + 'For Intersection you have to choose two data' + color.END)
        print('\n' * 1)
        print_data_options()
        x2 = int(input("Your input = "))

        if x2 in range(df.shape[0]):
            for i in range(1, df.shape[1]):
                print(f"for {df.columns[i]} press: {i}")

            x3 = int(input("Your input = "))
            if x3 in range(1, df.shape[1]):
                x4 = df.columns[x3]

                if x1 == '1':
                    op = df.loc[df.shape[0] - 1, x4] + df.loc[x2, df.columns[df.shape[1] - 1]] - df.loc[x2, x4]
                    print(f"From the given data Union of {df.loc[x2, df.columns[0]]} and {df.columns[x3]} is {op / total}")
                elif x1 == '2':
                    op = df.loc[x2, x4]
                    print(f"From the given data Intersection of {df.loc[x2, df.columns[0]]} and {df.columns[x3]} is {op / total}")

                total = df.loc[df.shape[0] - 1, df.columns[df.shape[1] - 1]]
                print("#" * 50)
                print('\n' * 2)
            else:
                print(color.RED + color.BOLD + 'MAY BE SOME INVALID INPUT' + color.END)
        else:
            print(color.RED + color.BOLD + 'MAY BE SOME INVALID INPUT' + color.END)

    elif x1 == '3':
        print(color.GREEN + color.BOLD + 'I THINK YOU GOT YOUR ANSWER' + color.END)
        print(color.GREEN + color.BOLD + 'THANK YOU FOR CHECKING THIS CODE' + color.END)
        print('\n' * 2)
        break

    else:
        print(color.RED + color.BOLD + 'MAY BE SOME INVALID INPUT' + color.END)
        print('\n' * 2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




