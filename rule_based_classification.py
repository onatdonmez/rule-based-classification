# Read the persona.csv file and show the general information about the dataset.
import pandas as pd
df = pd.read_csv('datasets/persona.csv')
df.head(5)
df.tail(5)
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

# How many unique SOURCE are there? What are their frequencies?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# How many unique PRICE are there?
df["PRICE"].nunique()

# How many sales were made from which PRICE?
df["PRICE"].value_counts()

# How many sales from which country?
df.groupby("COUNTRY").agg({"PRICE":"count"})

# How much was earned in total from sales by country?
df.groupby("COUNTRY").agg({"PRICE":"sum"})

# What are the sales numbers by SOURCE types?
df["SOURCE"].value_counts()

# What are the PRICE averages by country?
df.groupby(by = ["COUNTRY"]).agg({"PRICE":"mean"})

# What are the PRICE averages by SOURCEs?
df.groupby("SOURCE").agg({"PRICE":"mean"})

# What are the PRICE averages in the COUNTRY-SOURCE diffraction?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE":"mean"})

###############################################
# What are the average earnings in the diffraction of COUNTRY, SOURCE, SEX, AGE?
###############################################
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})

###############################################
# Sort the output by PRICE and assign it to agg_df
###############################################
agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE", ascending = False)

###############################################
# Convert the names in the index to variable names
###############################################
agg_df.reset_index(inplace = True)

###############################################
# Convert to age variable to categorical variable and add it to agg_df
###############################################
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, agg_df["AGE"].max()], labels = ["0_18", "19_23", "24_30", "31_40", "41_" +str(agg_df["AGE"].max())])

###############################################
# Identify new level_based customers(personas).
###############################################
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5] for row in agg_df.values]
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"}).reset_index()
agg_df["customers_level_based"].value_counts()

###############################################
# Segment new customers(personas).
###############################################
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels = ["D","C","B","A"])

agg_list = ["mean", "max", "min"]
agg_df.groupby("SEGMENT").agg({"PRICE" : agg_list})

# C segment analysis
agg_df["SEGMENT"] == "C"
agg_df[agg_df["SEGMENT"] == "C"]
agg_df["SEGMENT"].value_counts()

###############################################
# Classify new customers by segment and estimate how much revenue they can generate.
###############################################
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user2]
