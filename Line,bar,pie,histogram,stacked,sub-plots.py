#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv("company_sales_data.csv")
df


# In[10]:


#Exercise 1: Read Total profit of all months and show it using a line plot

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd

# load the data into a DataFrame
df = pd.read_csv("company_sales_data.csv")

# create a line plot of month_number vs total_profit
plt.plot(df['month_number'], df['total_profit'])

# add labels and title
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit by Month')

# display the plot
plt.show()


# In[15]:


# 2.	Exercise 2: Get total profit of all months and show line plot with the following Style properties



# In[14]:




# calculate total profit of all months
total_profit = df['total_units'] * df['total_profit'] / df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum(axis=1)
df['Total Profit'] = total_profit

# create line plot with style properties
plt.plot(df['month_number'], df['total_units'], linestyle='dotted', color='red',
         marker='o', markerfacecolor='red', markersize=8, linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Monthly Sales')
plt.legend(['Units Sold'], loc='lower right')

# show plot
plt.show()


# In[16]:


#3.	Exercise 3: Read all product sales data and show it using a multiline plot

plt.plot(df['month_number'], df['facecream'], color='blue', linewidth=3, label='Face Cream')
plt.plot(df['month_number'], df['facewash'], color='red', linewidth=3, label='Face Wash')
plt.plot(df['month_number'], df['toothpaste'], color='green', linewidth=3, label='Toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], color='purple', linewidth=3, label='Bathing Soap')
plt.plot(df['month_number'], df['shampoo'], color='orange', linewidth=3, label='Shampoo')
plt.plot(df['month_number'], df['moisturizer'], color='brown', linewidth=3, label='Moisturizer')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Product Sales')
plt.legend()


# In[17]:


#4.	Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot

plt.scatter(df['month_number'], df['toothpaste'], color='green', linewidth=3, label='Toothpaste')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Toothpaste Sales')
plt.show()


# In[19]:


#5.	Exercise 5: Read face cream and facewash product sales data and show it using the bar chart

plt.bar(df['month_number'], df['facecream'], color='green', linewidth=3, label='Toothpaste')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Face cream Sales')
plt.show()


# In[21]:


#6.	Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk



plt.bar(df['month_number'], df['bathingsoap'], color='blue', linewidth=3, label='Toothpaste')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('bathingsoap')
plt.show()

plt.savefig('bathing_soap_sales.png')


# In[23]:


#7.	Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges


plt.hist(df['total_profit'], bins=10, color='blue', linewidth=3)

plt.xlabel('Total Profit')
plt.ylabel('Frequency')
plt.title('Total Profit Histogram')
plt.show()


# In[26]:


##8.	Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart





last_year_df = df[df['month_number'] >= 12]
total_sales_data = last_year_df.iloc[:, 1:7].sum()

# create pie chart of total sales data
labels = total_sales_data.index.tolist()
sizes = total_sales_data.values.tolist()
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'pink']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Total Sales Data for Last Year')
plt.legend(loc='lower right')
plt.show()


# In[27]:


#9.	Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot


# select bathingsoap and facewash columns
bathingsoap_df = df[['month_number', 'bathingsoap']]
facewash_df = df[['month_number', 'facewash']]

# create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# plot bathingsoap data
ax1.plot(bathingsoap_df['month_number'], bathingsoap_df['bathingsoap'], color='blue', linewidth=3, marker='o')
ax1.set_xlabel('Month Number')
ax1.set_ylabel('Units Sold')
ax1.set_title('Bathing Soap Sales Data')

# plot facewash data
ax2.plot(facewash_df['month_number'], facewash_df['facewash'], color='green', linewidth=3, marker='o')
ax2.set_xlabel('Month Number')
ax2.set_ylabel('Units Sold')
ax2.set_title('Facewash Sales Data')

# adjust spacing between subplots
plt.subplots_adjust(wspace=0.4)





# In[28]:


#10.	Exercise Question 10: Read all product sales data and show it using the stack plot


# select product columns
products_df = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']]

# create stack plot
plt.stackplot(df['month_number'], products_df.values.T, labels=products_df.columns)

# set x-axis and y-axis labels and title
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Product Sales Data')

# show legend
plt.legend(loc='upper left')

plt.show()


# In[ ]:




