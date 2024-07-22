import pandas
#索引
data=pandas.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
# print(data)
#觀察資料
# print("資料型態",data.dtype)
# print("資料形狀",data.shape)
# print("資料索引",data.index)
# print("資料值",data.values)
# print("資料數量",data.size,len(data))
#根據索引取值
print(data.iloc[2],data.loc["c"])
#數字運算
print("平均值",data.mean())
print("加總",data.sum())
print("標準差",data.std())
print("最大值",data.max())
print("最小值",data.min())
print("中位數",data.median())
print("最大三個數\n",data.nlargest(3))
print("描述性統計\n",data.describe())
print("排序\n",data.sort_values())
#字串類資料
data2=pandas.Series(["你好","Python","Pandas"])
print(data2.str.lower())
print(data2.str.len())
print(data2.str.cat(sep=","))#每個元素用一個符號串聯
print(data2.str.contains("P"))#檢查每個元素是否包含P
print(data2.str.replace("您好","Hello"))
#多個修改
print(data2.str.replace("您好","Hello").str.replace("Pandas","Pandas2"))
