import pandas as pd
# load data
df=pd.read_csv("Raw_data.csv") 
# see  first rows

print(df.head())

# see column names
print(df.columns)

#see data types
print(df.dtypes)

#see missing values
print(df.isnull().sum())

#check duplicates
print("Duplicate rows:", df.duplicated().sum())

#CLEAN DATA
print("#FROM HERE IS THE CLEAN DATA #")
#Convert dates
df["Order Date"]= pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"]=pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

#convert Sales to  numeric
df["Sales"]=pd.to_numeric(df["Sales"], errors="coerce")

#convert Postal code to text not number
df["Postal Code"]= df["Postal Code"].astype("Int64").astype(str)

#check new data types
print(df.dtypes)

#check missing values
print (df.isnull().sum())

df.to_csv("cleaned_data.csv",index=False )