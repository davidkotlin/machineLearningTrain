import pandas
#series
# data=pandas.Series([1,2,3,4,5,6,7,8,9,10])
#list後面加index=[編號]，指定索引
calories = {"day1": 420, "day2": 380, "day3": 390}
print(calories[["day1"]])
#設定索引法二
# print(data,"\n",data[0],"\n",data[1:3],"\n",data[1:11:2])
# #series操作
# print(data.max())
# print(data.min())
# print(data.mean())
# print(data.std())
# print(data.median())
# print(data.describe())#全部基本統計資料
# data=data==5#比較運算，得到布林值
# print(data)
#dataframe
data=pandas.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,40000,50000]
})
#可在大括號後面加index=[編號]，指定索引
# print(data)
# #取得特定欄位
# print(data["name"])
# #取得特定列
# print(data.iloc[0])
# print(data.iloc[0:2])
print(data.iloc[0][0])
print(data[["name","salary"]])