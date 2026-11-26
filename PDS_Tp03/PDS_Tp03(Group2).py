#=====================================================
# TP3: Working with pandas Series and DataFrames
# Group 2
# Group Members:
# 1. BOEUN Piseth
# 2. CHENG Sokvisal
# 3. CHHEAN Ravy
# 4. HENG Limhong
# 5. HIN Panha
#=====================================================

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent

# =====================================================
# Problem 3: Build and Inspect the Student Table
# =====================================================

# Step 1: Read the file and print the shape of the table (rows, columns)
df = pd.read_csv(DATA / "students.csv")
print("Shape:", df.shape)

# Step 2: Preview the first 3 rows with head()
print(df.head(3))

# Step 3: List the column namees and count the studeents
print("Columns:", df.columns.tolist())
print("Students:", len(df))

# Step 4: Summarise the numeric columns age and gpa with describe()
print(df[["age", "gpa"]].describe().round(2))

# Step 5: Which majors are there, and how many students are in each?
print("Majors:", df["major"].unique().tolist())
print(df["major"].value_counts())

# =====================================================
# Problem 4: Selecting Columns and Rows
# =====================================================
from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent
# Step 1: Read students.csv. One column gives a Seeries; a list of colmns gives a DataFrame
df = pd.read_csv(DATA / "students.csv")
print(df["name"].tolist())
print(df[["name", "gpa"]].head(3))

# Step 2: With .loc[rows, columns], select the rows 0 to 2 and the columns name and major
print(df.loc[0:2, ["name", "major"]])

# Step 3: With .iloc, select the last 2 rows and the first 3 columns, by position
print(df.iloc[-2:,:3])

# Step 4: Put a condition inside .loc to get the GPA of Malis as one number
gpa = df.loc[df["name"] == "Malis", "gpa"].item()
print("GPA of Malis:", gpa)

# Step 5: Make the names the index with set_index(), then read one cell by its labels
by_name = df.set_index("name")
print("Rith lives in", by_name.loc["Rith", "city"])
