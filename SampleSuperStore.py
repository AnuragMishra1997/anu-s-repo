#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('SampleSuperstore.csv')
df=pd.DataFrame(data)
print(df.head())
df.tail()


# In[ ]:


#Shape of the DataSet
df.shape


# In[ ]:


#A concise info of the Dataset
df.info()


# In[ ]:


#Getting Descriptive Statistics Summary
df.describe()


# In[ ]:


df.Category.unique()


# In[ ]:


df.nunique()


# In[ ]:


#Checking For NULL values
df.isnull().sum()


# In[ ]:


#Top 10 Highest profit earning Areas
print(df.nlargest(10,['Profit']))

#top 5 lowest profit areas
print(df.nsmallest(5,['Profit']))


# In[ ]:


sns.relplot(x='Sales',y='Profit',hue='Ship Mode',data=df)


# In[ ]:


sns.distplot(df['Quantity'],bins=5)


# In[ ]:


sns.catplot(x='Discount',kind='box',data=df)


# # Grouping Postal code with Sales
# 

# In[ ]:


df_PostalCodeSales=df.groupby('Postal Code').sum()['Sales'].reset_index()
df_PostalCodeSales


# In[ ]:


# trend of Postal Code with Sales
plt.figure(figsize=(15,6))
plt.plot(df_PostalCodeSales['Postal Code'],df_PostalCodeSales['Sales'])
plt.show()


# # Ship Mode with Sales

# In[ ]:


#most preffered Ship Mode
sns.countplot(df['Ship Mode'])


# In[ ]:


#Grouping Ship Mode with SALES
ShipMode_Sales=pd.DataFrame(df.groupby('Ship Mode').sum()['Sales'].reset_index())
ShipMode_Sales


# In[ ]:


ShipMode_Sales=ShipMode_Sales.sort_values('Sales',ascending=False)
ShipMode_Sales


# In[ ]:


ShipMode_Sales.plot(x="Ship Mode", y=["Sales"], kind="bar")
plt.show()


# In[ ]:


#Grouping Sub_Category with Sales
prod_Sales=pd.DataFrame(df.groupby('Sub-Category').sum()['Sales'].reset_index())
prod_Sales


# In[ ]:


#Sorting Products by Sales
prod_Sales=prod_Sales.sort_values('Sales',ascending=False)
prod_Sales[:10]


# # Top 10 Sub-Category by Sales
# 

# In[ ]:


prod_Sales[:10].plot(x="Sub-Category", y=["Sales"], kind="bar")
plt.show()


# # which are the top 10 most Selling Products?

# In[ ]:


Selling_Products=pd.DataFrame(df.groupby('Sub-Category').sum()['Quantity'].reset_index())
Selling_Products
Selling_Products=Selling_Products.sort_values('Quantity',ascending=False)
Selling_Products[:10]


# # Most profitable Category and Sub-Category

# In[ ]:


#Grouping Category and Sub-Category
Cat_SubCat_Profit=pd.DataFrame(df.groupby(['Category','Sub-Category']).sum()["Profit"])
Cat_SubCat_Profit


# In[ ]:


#Sorting Category,Sub-Category with Profit
Cat_SubCat_Profit.sort_values(['Category','Profit'],ascending=False)


# # Region with Profit and Sales

# In[ ]:


#Grouping region with Profit
Reg_Profit=pd.DataFrame(df.groupby(['Region']).sum()["Profit"])
Reg_Profit


# In[ ]:


#Sorting
Reg_Profit.sort_values(['Profit','Region'],ascending=False)


# # Top 5 Least Selling Products

# In[ ]:


Least_sell_Products=pd.DataFrame(df.groupby('Sub-Category').sum()['Quantity'].reset_index())
Least_sell_Products
Least_sell_Products=Least_sell_Products.sort_values('Quantity',ascending=True)
Least_sell_Products[:5]


# # most used Segment type

# In[ ]:


sns.countplot(df['Segment'])


# In[ ]:


#Grouping Segment with Sales 
Segment_Sales=pd.DataFrame(df.groupby('Segment').sum()['Sales'].reset_index())
Segment_Sales


# In[ ]:


#Sorting
Segment_Sales.sort_values(['Sales','Segment'],ascending=False)


# In[ ]:


Segment_Sales.plot(x="Segment", y=["Sales"], kind="bar")
plt.show()


# # Segment with Profit

# In[ ]:


Seg_Profit=pd.DataFrame(df.groupby('Segment').sum()['Profit'].reset_index())
Seg_Profit


# In[ ]:


Seg_Profit.plot(x="Segment", y=["Profit"], kind="bar")
plt.show()


# # 5 States with least Sales

# In[ ]:


#Grouping States with Sales
State_Sales=pd.DataFrame(df.groupby('State').sum()['Sales'])
State_Sales


# In[ ]:


#Sorting
State_Sales.sort_values(['Sales','State'],ascending=False)


# In[ ]:


State_Sales.nsmallest(5, ['Sales'])


# In[ ]:




