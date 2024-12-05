import pandas as pd

retail_data = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2009-2010')
print(retail_data.head())
print(f"Shape of data: {retail_data.shape}")

#Check for missing values
print(retail_data.isnull().sum())
retail_data.dropna(inplace=True)
print(retail_data.isnull().sum())  

#Remove duplicate records
print(f"Total duplicate rows: {retail_data.duplicated().sum()}")
retail_data.drop_duplicates(inplace=True)
print(f"Total duplicate rows after removal: {retail_data.duplicated().sum()}")

#Fix Data Types
retail_data['InvoiceDate'] = pd.to_datetime(retail_data['InvoiceDate'])
retail_data['Quantity'] = retail_data['Quantity'].astype(int)
retail_data['Price'] = retail_data['Price'].astype(float)
retail_data['TotalPrice'] = retail_data['Quantity'] * retail_data['Price']

#Filter out invalid data
filter_data = retail_data[retail_data['Quantity'] > 0]

#Saving the cleaned dataset
filter_data.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved successfully!")

#verifying the cleaned data
cleaned_data = pd.read_csv('cleaned_data.csv')
print(cleaned_data.head())
print(f"Shape of cleaned data: {cleaned_data.shape}")







