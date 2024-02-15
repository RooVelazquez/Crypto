import pandas as pd              #Brings in the Pandas library and aliases it as 'pd' for data manipulation.
import matplotlib.pyplot as plt  #Importing Matplotlib for plotting the data
import seaborn as sb             #Import seaborn for plotting graphs or make visualizations
import math as math              #import for mathamatical operations

df = pd.read_csv(r'C:\Users\kiran\OneDrive\Desktop\crypto prediction\main_venkat\Cryptocurrency-Price-Prediction\Excel DB\Crypto_data_info.csv')
df.head()                        #Shows the initial rows of the DataFrame, offering a quick view of the dataset.
df.shape                         #Provides the number of rows and columns in the DataFrame, indicating its size.
df.describe()                    #Presents summary statistics for numerical columns, revealing central tendencies and data spread.

print(df)

# Set the figure size to 10x5 inches.
plt.figure(figsize=(10,5))

# Plot the 'close' column from the DataFrame.
plt.plot(df['close'])  

# Set the title of the plot with a fontsize of 15.
plt.title('Bitcoin Close price.', fontsize=15)

# Label the y-axis as 'Price in dollars.'
plt.ylabel('Price in dollars.')  

#display the plot
plt.show()

print(df.isnull().sum())

#We create a list named features that will contain the features or columns that we want to explore
features = ['open', 'high', 'low', 'close']

#This creates a figure and axis grid with a specific size of 20 inches in width and 10 inches in height.
plt.subplots(figsize=(20, 10))
# Iterate over each feature in the 'features' list
for i, col in enumerate(features):
    # Create subplots within the grid, with 2 rows, 2 columns, and index i + 1
    plt.subplot(2, 2, i + 1)
    # Plot a distribution plot (histogram and kernel density estimate) for the current feature
    #with this we can visualize the distribution of each feature data
    sb.distplot(df[col])
#This displays the plot grid created by the previous subplots.
plt.show()

#convting object [date] column format to dateTime format
df['date'] = pd.to_datetime(df['date']) 

# Extract the year from the 'date' column using the dt accessor in pandas
df['year'] = df['date'].dt.year

# Extract the month from the 'date' column using the dt accessor in pandas
df['month'] = df['date'].dt.month

# Extract the day from the 'date' column using the dt accessor in pandas
df['day'] = df['date'].dt.day

# Print the first few rows of the DataFrame to see the changes
print(df.head())

# Group the DataFrame 'df' by the 'year' column and calculate the mean of each numeric column for each group
#numeric_only is to calculate mean only for numbers
data_grouped = df.groupby(['year']).mean(numeric_only=True)
print(data_grouped)

# Create a new figure and subplots with a specific size (20x10 inches)
plt.subplots(figsize=(20, 10))

# Iterate over each column ('open', 'high', 'low', 'close') and its corresponding index
for i, col in enumerate(['open', 'high', 'low', 'close']):
    # Create subplots in a 2x2 grid, with each subplot representing one of the numeric columns
    plt.subplot(2, 2, i + 1)

    # Plot a bar chart for the current column using the grouped data
    data_grouped[col].plot.bar()

# Display the plot
plt.show()
# This are the box plots for open..similar can be done for close,low,high.
plt.title('This is a boxplot of Crypto Open Prices includes outliers')# This is the Title for Boxplot
plt.xlabel('open price') #label for open boxplot
sb.boxplot(data=df['open'], showfliers=True ,orient='h') #df reads column open ,showflies shows outliers and orientation will be horizontal(h) or vertical(v)
#Displays the plot
plt.show()

#Correlation for bitcoin crypto 
plt.figure(num="Correlation HeatMap")
print(df.info())
corr = df.loc[df['crypto_name'] == 'Bitcoin'].iloc[:,1:].corr(numeric_only=True).round(2)
sb.heatmap(corr, annot=True)
plt.title("Correlation HeatMap for BitCoin")


#ploting graph to check correlation
plt.figure(num="Scatter Plot")
for index, val in enumerate(['open', 'high', 'low', 'close', 'volume']):
    plt.subplot(3,2,index+1)
    plt.scatter(df.loc[df['crypto_name'] == 'Bitcoin'][val], df.loc[df['crypto_name'] == 'Bitcoin']['marketCap'])
    plt.xlabel(val)
    plt.ylabel('marketCap')
    plt.title(f'Scatter plot between {val} and marketcap ')
plt.subplots_adjust(left=0.1,
                    bottom=0.08, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.4)

#==================== NOTE =====================
#
# from the above figure:- 5 in plot betweeen marketCap and volumn
# the reason for volumne is having correlation 0.7 is because of an outliear
#
#==================== NOTE =====================

#boxplot to check outliers with whisker_length(whis) of 1.5(default value)
plt.figure(num="Box plot")
for index, val in enumerate(['open', 'high', 'low', 'close', 'volume', 'marketCap']):
    plt.subplot(3,2,index+1)
    plt.boxplot(pd.array(df.loc[df['crypto_name'] == 'Bitcoin'][val]), vert = False)
    plt.title(f'Box plot of {val} ')
plt.subplots_adjust(left=0.1,
                    bottom=0.08, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.4)
plt.show()

#checking null values in Bitcoin dataset
print(df.loc[df['crypto_name'] == 'Bitcoin'].isnull().sum())
