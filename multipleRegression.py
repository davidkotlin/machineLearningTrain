import pandas
from sklearn import linear_model
from scipy import stats
df = pandas.read_csv("multipleRegressionData.csv")
# print(df,df.shape)
#csv檔中選擇重量和體積，這些是模型的特徵（輸入變數）
X = df[['Weight', 'Volume']]
# print(X)
#csv檔中選擇CO2，，即我們想要預測的值（輸出變數）
y = df['CO2']
# print(y)
# 創建並擬合模型
regr = linear_model.LinearRegression()
regr.fit(X, y)#使用特徵 X 和目標變數 y 擬合模型，讓模型學習數據中的關係。
"""模擬維空間中的直線"""
# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedCO2 = regr.predict([[2300, 1300]])

# print(predictedCO2)
# new_data = pandas.DataFrame({'Weight': [2300,2400], 'Volume': [1300,1400]})
# predictedCO2 = regr.predict(new_data)
print(regr.coef_,regr.coef_[0],regr.coef_[1])#印出重量與體積的回歸係數
print(regr.intercept_)
# print(predictedCO2)
r_value, _ = stats.pearsonr(df['Weight'], df['CO2'])
print(f"Weight 和 CO2 的 R 值: {r_value}")
correlation_matrix = df[['Weight', 'Volume', 'CO2']].corr()
print(correlation_matrix)