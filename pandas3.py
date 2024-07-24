import pandas
#資料索引
data=pandas.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
},index=["a","b","c"])
# print(data)
#觀察資料
# print("資料數量",data.size)
# print("資料形狀",data.shape)
# print("資料索引",data.index)
# print("欄目名稱",data.columns)
#取得列
# print("取的第二列\n",data.iloc[1])
# print("取的第c列\n",data.loc["c"])
#取得欄
# print("取得name欄\n",data["name"])
#取出後進行series運算
# names=data["name"]
# print(names.str.upper())
# salarys=data["salary"]
# print(salarys.mean())
#建立新欄位
data["bonus"]=data["salary"]*0.1
data["age"]=pandas.Series([20,21,22],index=["a","b","c"])
# 或data["age"]=[20,21,22]
print(data)
# print(data[["salary","age","bonus"]].corr())#計算相關係數
# #將dataframe的值變為布林值
# # colors = pandas.DataFrame({'color': ['blue', 'red']})
# # print(colors)
# # dummies = pandas.get_dummies(colors, drop_first=True)

# # print(dummies)
# colors = pandas.DataFrame({'color': ['blue', 'red', 'green']})
# # dummies = pandas.get_dummies(colors, drop_first=True)#drop_first=True: 这个参数表示在生成one-hot编码时，去掉第一个类别
# dummies = pandas.get_dummies(colors,drop_first=False)
# # # 手動去掉第二個類別的列（'color_red'）
# # dummies = dummies.drop(columns=['color_red'])
# dummies['color'] = colors['color']#將colors的顏色哪一欄加入dummies成為新的一欄

# print(dummies)