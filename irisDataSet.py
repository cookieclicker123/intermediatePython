import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filePath = '/Users/seb/Documents/iris.csv'

pd.set_option('display.max_rows', None)


# Read the data
data = pd.read_csv(filePath)

print("-------------------")
data['SepalLengthCm'] = data.apply(lambda row: row['SepalLengthCm'] * 10 
                                   if row['Species'] == 'Iris-setosa' 
                                   else row['SepalLengthCm'], axis=1)
print("-------------------")
print(data)
print("-------------------")
data.info()
print("-------------------")
print(data.describe())
print("-------------------")
# what does the following line do

print(data.isnull().sum())


#help me plot the mean lengths
#sns.histplot(data['SepalLengthCm'])
#plt.title('Distribution of Sepal Length')
#plt.xlabel('Sepal Length Value')
#plt.ylabel('Frequency')

#plt.show()

#help me plot themean widths, but instead of a histogram, I want a curve

#sns.kdeplot(data['SepalWidthCm'], shade=True)
#plt.title('Distribution of Sepal Width')
#plt.xlabel('Sepal Width Value')
#plt.ylabel('Frequency')

#plt.show()

# Add a new column 'SepalArea' to the DataFrame
data['SepalArea'] = data['SepalLengthCm'] * data['SepalWidthCm']

# Display the first few rows of the DataFrame to verify the new column has been added
print(data.head())


#help me dispaly the largest value in the sepal area column
print("-------------------")
print("Largest Area: " + str(data['SepalArea'].max()))
print("-------------------")
print("-------------------")
print("Sepal Area:\n" + str(data['SepalArea'].describe()))
print("-------------------")
print(data['Species'].value_counts())
print("-------------------")
pivot = data.pivot_table(index='Species', columns='SepalLengthCm', values='SepalArea', aggfunc='mean')
print(pivot)
print("-------------------")
data['SepalLengthCm'] = data['SepalLengthCm'].apply(lambda x: x * 10)
print("-------------------")
# Use a histogram to visualize the distribution of 'SepalArea'
sns.histplot(data['SepalArea'])
plt.title('Distribution of Sepal Area')
plt.xlabel('Sepal Area Value')
plt.ylabel('Frequency')
plt.show()

# Use a KDE plot to visualize the distribution of 'SepalArea'
sns.kdeplot(data['SepalArea'], shade=True)
plt.title('Distribution of Sepal Area')
plt.xlabel('Sepal Area Value')
plt.ylabel('Frequency')
plt.show()

