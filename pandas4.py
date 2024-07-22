import pandas
#篩選Series
# data=pandas.Series([30,15,20])
# condition=[True,False,True]
# # filterData=data[condition]
# filterData=data[data>18]
# print(filterData)
# data=pandas.Series(["你好","Python","Pandas"])
# condition=data.str.contains("P")
# filterData=data[condition]
# print(filterData)
#篩選dataframe
data=pandas.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
# condition=data["salary"]>=40000
condition=data["name"]=="Amy"
filterData=data[condition]
print(filterData)