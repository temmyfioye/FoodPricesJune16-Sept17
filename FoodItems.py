
# coding: utf-8


#import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#parse and read the file
df = pd.read_csv('..insert file path here') #reading the file
df.info() #parsing it

print (df.ItemLabels)

#food items of interest are: Tomato, Medium Grain Rice, White Gari (sold loose), Yam Tuber, 
#Brown Beans (sold loose) and Onion bulb

global start_month
global end_month
global timeperiod
global xlabel 
start_month = input('Numerical value of start month using column values above: ') #first month on the plot
start_month = int(start_month)
last_month = input('Numerical value of end month using column values above: ') #last month on the plot
last_month = int(last_month)+1
months = df.columns.values[start_month:last_month]
timeperiod = len(months) #number of months
f_month = months[0]
l_month = months[-1]
print(f_month)
print(l_month)
print (months)
print ('Number of months is ', timeperiod)
xlabel = 'Timeline: ' + f_month + ' to ' + l_month
print(xlabel)

# Function definition is here    
def acceptitem( itemlabel ):
    fooditem = df[df.ItemLabels == itemlabel] #getting the data for entered item
    fooditem = fooditem.iloc[:,start_month:last_month]  #selecting data from june to last month
    fooditem = fooditem.values.T.tolist() #put the data in a list
    return fooditem;

itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y1 = acceptitem( itemlabel )
itemlabel1 = itemlabel
print (itemlabel, '= ', y1)

#accepting user input for second food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y2 = acceptitem( itemlabel )
itemlabel2 = itemlabel
print (itemlabel, '= ', y2)

#accepting user input for third food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y3 = acceptitem( itemlabel )
itemlabel3 = itemlabel
print (itemlabel, '= ', y3)

#accepting user input for fourth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y4 = acceptitem( itemlabel )
itemlabel4 = itemlabel
print (itemlabel, '= ', y4)

#accepting user input for fifth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y5 = acceptitem( itemlabel )
itemlabel5 = itemlabel
print (itemlabel, '= ', y5)

#accepting user input for sixth food item
itemlabel = input('Enter a food item as specified in the label output above: ')
#calling the function acceptitem
y6 = acceptitem( itemlabel )
itemlabel6 = itemlabel
print (itemlabel, '= ', y6)


#plotting the data
x_axis = np.arange(timeperiod)
plt.xticks(x_axis, months, rotation='vertical')
plt.xlabel(xlabel)
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
