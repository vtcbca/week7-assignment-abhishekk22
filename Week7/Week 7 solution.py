import csv
with open ("S://22bca22//product.csv",'w') as f:
    data=csv.writer(f)
    header=["prod_no","prod_name","jan","feb","mar","apr","may","jun"]
    data.writerow(header)
    for i in range(12):
        prod_no=int(input("Enter product no:"))
        prod_name=input("Enter name:")
        jan=int(input("Enter product selling of jan:"))
        feb=int(input("Enter product selling of feb:"))
        mar=int(input("Enter product selling of mar:"))
        apr=int(input("Enter product selling of apr:"))
        may=int(input("Enter product selling of may:"))
        jun=int(input("Enter product selling of jun:"))
        record=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        data.writerow(record)
        
with open("S://22ba22//product.csv",'r')as f1:
    content=csv.reader(f1)
    for i in content:
        print(i)

#2.Create dataframe.        
import pandas as pd
df=pd.read_csv("S:\22bca22\product.csv")
print(df)

# 3. Change Column Name Product No, Product Name, January, February, March, April, May, June.
df.columns=["Product_no","Product_name","January","February","March","April","May","June"]
print(df)

# 4.  Add column "Total Sell" to count total of all month and "Average Sell"
df["Total sell"]=df["January"]+df["February"]+df["March"]+df["April"]+df["May"]+df["June"]
print(df)
df["Average sell"]=df["Total sell"]/6
print(df)

# 5. Add 2 row at the end.
df.loc[12],df.loc[13]=[13,"laptop adptor",8000,10000,6000,7000,9000,12000,52000,8666.66],[14,"SSD",5000,6000,5000,4000,2000,8000,30000,5000]
print(df)

# 6.Add 2 row after 3rd row.
df.loc[2.5]=[3,"charging",8000,6000,8000,5000,4000,6000,37000,6166.66]
print(df)
df.loc[3.5]=[4,"SSD",8000,6000,9000,5000,8000,7000,43000,7166.666]
print(df)

# 7.Add 2 row after 3rd row.
df.head(5)
print(df)

# 8. Print Last 5 row.
df.tail(5)
print(df)

# 9. Print row 6 to 10.
df.iloc[5:9]
print(df)

# 10.Print only product name.
print(df.product_name)

# 11. Print sell of January month with product id and product name.
print(df[["product_no","product_name","january"]])

# 12.  Print only those product id , product name where january sell is > 5000 and February sell is >8000
print(df[df["january"]>5000 and df["february"]>8000][["product_no","product_name"]])

# 13. Print record in sorting order of Product name.
print(df.sort_values(by=["product_name"]))

# 14. Display only odd index number column record.
print(df.iloc[1::2])

# 15. Display alternate row.
print(df.iloc[::2])


