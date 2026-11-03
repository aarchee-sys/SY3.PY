import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("customer_churn.csv")


print(data.head())

print(data.info())

print(data.describe())


print(data.isnull().sum())

data = data.drop_duplicates()

data = data.fillna(0)


print(data['Churn'].value_counts())


sns.countplot(x='Churn', data=data)
plt.title("Customer Churn")
plt.show()

sns.countplot(x='Contract', hue='Churn', data=data)
plt.title("Churn by Contract")
plt.show()


sns.histplot(data=data, x='tenure', hue='Churn')
plt.title("Churn by Tenure")
plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=data)
plt.title("Monthly Charges")
plt.show()

sns.heatmap(data.select_dtypes('number').corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()


data.to_csv("cleaned_data.csv", index=False)

print("Data cleaning and analysis completed!")
