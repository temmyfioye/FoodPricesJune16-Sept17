
# coding: utf-8

# In[1]:

#import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

#parse and read the file
df = pd.read_csv('C://Users//admin//Documents//food_prices_watch.csv') #reading the file
df.info() #parsing it


# In[3]:

timeline = ('Jun-16','Jul-16', 'Aug-16', 'Sep-16','Oct-16','Nov-16','Dec-16','Jan-17','Feb-17','Mar-17','Apr-17','May-17','Jun-17', 'Jul-17', 'Aug-17', 'Sep-17') #this is a list of the labels that will appear in the chart


# In[4]:

print (df.ItemLabels)


# In[5]:

#food items of interest are: Tomato, Medium Grain Rice, White Garri (sold loose), Yam Tuber, 
#Brown Beans (sold loose) and Onion bulb


# In[6]:

# Function definition is here
def acceptitem( itemlabel ):
    fooditem = df[df.ItemLabels == itemlabel] #getting the data for entered item
    fooditem = fooditem.iloc[:,6:]  #selecting data for June 2016-September 2017
    fooditem = fooditem.values.T.tolist() #put the data in a list
    return fooditem;


# In[7]:

#accepting user input for first food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y1 = acceptitem( itemlabel )
itemlabel1 = itemlabel
print (itemlabel, '= ', y1)


# In[8]:

#accepting user input for second food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y2 = acceptitem( itemlabel )
itemlabel2 = itemlabel
print (itemlabel, '= ', y2)


# In[9]:

#accepting user input for third food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y3 = acceptitem( itemlabel )
itemlabel3 = itemlabel
print (itemlabel, '= ', y3)


# In[10]:

#accepting user input for fourth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y4 = acceptitem( itemlabel )
itemlabel4 = itemlabel
print (itemlabel, '= ', y4)


# In[11]:

#accepting user input for fifth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y5 = acceptitem( itemlabel )
itemlabel5 = itemlabel
print (itemlabel, '= ', y5)


# In[13]:

#accepting user input for sixth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y6 = acceptitem( itemlabel )
itemlabel6 = itemlabel
print (itemlabel, '= ', y6)


# In[15]:

#plotting the data
x_axis = np.arange(len(timeline))
plt.xticks(x_axis, timeline, rotation='vertical')
plt.xlabel('Timeline (June 2016-September 2017)')
plt.ylabel('Price per KG')
plt.ylim(150, 500)
plt.title('Changes in price of selected food items')
plt.plot(x_axis,y1, '-', color='#de3242', label= itemlabel1) #in a shade of red
plt.plot(x_axis,y2, '-', color='#a52a2a', label= itemlabel2) #brown shade
plt.plot(x_axis,y3, '-', color='#00007f', label= itemlabel3) #blue shade
plt.plot(x_axis,y4, '-', color='#666600', label= itemlabel4) #red and green mix
plt.plot(x_axis,y5, '-', color='#008000', label= itemlabel5) #green
plt.plot(x_axis,y6, '-', color='#800080', label= itemlabel6) #purple
plt.legend(loc='upper left')
#plt.savefig('C://Users//admin//Documents//food-prices-2.jpg')
plt.show()


# In[ ]:



