#標準化
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

df = pandas.read_csv("multipleRegressionData.csv")
X = df[['Weight', 'Volume']]
#計算資料 X 的平均值和標準差來轉換資料 X，將每個特徵標準化
scale = StandardScaler()#不直接引用StandardScaler，確保適配相同數據
scaledX = scale.fit_transform(X)
# print(scaledX)
# scale.fit(X)=>計算 X 的均值和標準差
# print(scale.fit(X))
# print(scale.mean_)# meanX = scale.mean_#平均
# print(scale.scale_)# stdX = scale.scale_#標準差
# transform(X)=>將 X 中的每個數據點標準化，得到的結果存儲在 scaledX 中
# print(scale.transform(X))

# print(scaledX)
# print(meanX)
# print(stdX)
y = df['CO2']

regr = linear_model.LinearRegression()
#使用標準化後的特徵 scaledX 和目標變數 y 訓練模型
regr.fit(scaledX, y)
#預測
# new_data = pandas.DataFrame({'Weight': [2300], 'Volume': [1.3]})
new_data = pandas.DataFrame({'Weight': [2300,2400], 'Volume': [1.3,1.5]})
scaled = scale.transform(new_data)
# #對scaled進行預測[0]是第一個，也只有一個，所以結果同predictedCO2 = regr.predict(scaled)
# predictedCO2 = regr.predict([scaled[0]])
predictedCO2 = regr.predict(scaled)

print(predictedCO2)
print(scaled)