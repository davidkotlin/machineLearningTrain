# import pandas
# cars = pandas.read_csv('multipleRegressionData.csv')
# #改變csv檔的索引
# #cars.index=index=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"]
# print(cars.to_string())
# #.get_dummies() 統計每個car欄中有幾個品牌
# ohe_cars = pandas.get_dummies(cars[['Car']])

# print(ohe_cars.to_string())
#加入汽車品牌的預測模型
import pandas
from sklearn import linear_model

cars = pandas.read_csv("multipleRegressionData.csv")
ohe_cars = pandas.get_dummies(cars[['Car']])
#print(ohe_cars.shape[1])看出車種有17個
#把ohe_cars加入X，根據列
X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']
# print(X)
# print(X.shape)
regr = linear_model.LinearRegression()
regr.fit(X,y)
# predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

#dataframe形式輸入預測值
# input_data = pandas.DataFrame({
#     'Volume': [1300,1200],
#     'Weight': [2300,2100],
#     'Car_Audi': [0,1],
#     'Car_BMW': [0,0],
#     'Car_Fiat': [0,0],
#     'Car_Ford': [0,0],
#     'Car_Honda': [0,0],
#     'Car_Hundai': [0,0],
#     'Car_Hyundai': [0,0],
#     'Car_Mazda': [0,0],
#     'Car_Mercedes': [0,0],
#     'Car_Mini': [0,0],
#     'Car_Mitsubishi': [0,0],
#     'Car_Opel': [0,0],
#     'Car_Skoda': [0,0],
#     'Car_Suzuki': [0,0],
#     'Car_Toyoty': [0,0],
#     'Car_VW': [1,0],
#     'Car_Volvo': [0,0], 
# })
"""
以上方式過於複雜
"""
#print(ohe_cars.columns,ohe_cars.shape[1])#ohe_cars.columns為所有欄位(車種)名稱
# 提取one-hot編碼列名
car_columns = [col for col in ohe_cars.columns]

# 創建一個DataFrame作為預測輸入
input_data = pandas.DataFrame({
    'Volume': [1300],
    'Weight': [2300],
    **dict.fromkeys(car_columns, 0)  # 一開始先將所有的車種都設為0
})
#dict.fromkeys(car_columns, 0)為將列表快速初始化為字典的方法
#**用於將字典中，key的值快速變為dataframe中的欄名
# 在對特定的車種輸入1
input_data['Car_VW'] = 1
predictedCO2 = regr.predict(input_data)
print(predictedCO2)