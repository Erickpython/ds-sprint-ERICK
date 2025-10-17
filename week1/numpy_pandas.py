import numpy as np

arr1 = np.array([10,20,30,40,50])  #1D array
arr2 = np.array([[1,2,3],[4,5,6]])  #2D array

print("1D Array:", arr1)
print("2D Array:\n", arr2)  
print("Shape of 1D Array:", arr1.shape)
print("Shape of 2D Array:", arr2.shape)
print("Data type of 1D Array:", arr1.dtype) 
print("Data type of 2D Array:", arr2.dtype)

# array operations 
print ("Mean:", np.mean(arr1))
print ("Sum:", np.sum(arr2))
print ("Max:", np.max(arr1))
print ("Min:", np.min(arr2))
print ("Standard Deviation:", np.std(arr1))
print ("Transpose of 2D Array:\n", np.transpose(arr2))  

# indexing, slicing and broadcasting 
print("The firt 3 elements: ",arr1[:3])
print("Multiply all elements by 2", arr1*2)

matrix = np.arange(1, 10).reshape(3,3)
print("Matrix:\n", matrix)
print("Row 2:", matrix[1])
print("column 3:", matrix[:, 2])

# RANDOM AND STATISTICAL SIMULATIONS
random_nums = np.random.randint(1, 100, (4, 4))
print("Random Numbers:\n", random_nums)
print("Colunm means: ", np.mean(random_nums, axis=0))
print ("Row sums:", np.sum(random_nums, axis=1))


# PANDAS ESSENTIALS 
import pandas as pd

# load titanic data from seaborn
import seaborn as sns
titanic = sns.load_dataset('titanic')

#preview data 
print(titanic.head())
print(titanic.info())
print(titanic.describe())

# data selection and filtering
subset = titanic[['survived', 'age', 'fare', 'sex']]
print(subset.head())
print(subset.info())

# filter passengers older than 50
older_than_50 = titanic[titanic['age'] > 50]
print (older_than_50.shape)

# sorting, grouping and aggregation
sorted_titanic = titanic.sort_values(by='age', ascending=False)

#group by gender and calculate mean fare
grouped = titanic.groupby('sex')['fare'].mean()
print("Mean fare by gender:\n", grouped)

# data cleaning 
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())

# drop rows with missing embarked values
titanic.dropna(subset=['embarked'], inplace=True)

# create derived columns 
# add colum for age group 
titanic['age_group'] = pd.cut(titanic['age'], bins=[0, 12, 18, 35, 60, 90], labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
print (titanic[['age', 'age_group']].head())

# barchrt for survival rate by age group
import matplotlib.pyplot as plt
age_group_survival = titanic.groupby('age_group')['survived'].mean()
age_group_survival.plot(kind='bar')
plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.show()