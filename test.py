# import numpy as np
# from sklearn.linear_model import LinearRegression

# # 數據
# x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y = np.array([1, 3, 2, 5, 4])

# # 創建並訓練模型
# model = LinearRegression()
# model.fit(x, y)

# # 獲得係數
# coefficients = model.coef_
# print(coefficients)  # 這裡將輸出一個單一的值
# import pandas as pd

# # 創建一個 DataFrame
# data = {
#     'Car': ['Toyota', 'Mitsubishi', 'Skoda'],
#     'Model': ['Aygo', 'Space Star', 'Citigo'],
#     'Volume': [1000, 1200, 1000],
#     'Weight': [790, 1160, 929],
#     'CO2': [99, 95, 95]
# }

# df = pd.DataFrame(data)

# print(df)
# x = [1, 2, 3, 4, 5]
# # 将列表元素转换为字符串
# stringX = list(map(str, x))

# # 创建一个新的列表，每两个元素组成一个子字符串
# grouped = [stringX[i] + stringX[i+1] for i in range(0, len(stringX) - 1, 2)]
# print(grouped)
# # 如果列表长度是奇数，添加最后一个元素
# if len(stringX) % 2 != 0:
#     grouped.append(stringX[-1])

# # 使用逗号连接所有子字符串
# result = ",".join(grouped)
# print(result)
# import pandas
# series=pandas.Series(["!","@","#"],name="symbol")
# dataframe=pandas.DataFrame({
#     "name":["Amy","Bob","Charles"],
#     "salary":[30000,50000,40000]
# })
# result=pandas.concat([dataframe[["name","salary"]],series],axis=1)
# print(result)
# 假設 car_columns 是一個包含one-hot編碼列名的列表
# car_columns = ['Car_A', 'Car_B', 'Car_C', 'Car_D']

# # 使用 dict.fromkeys() 創建字典，所有鍵的值都初始化為 0
# initial_dict = dict.fromkeys(car_columns, 0)
# print(initial_dict)
# initial_dict["Car_A"]=100

# print(initial_dict)
字典={"a":1,"b":2}
# 初始化字典=dict.fromkeys(字典,0)
初始化字典=dict.fromkeys(字典.keys(),0)
print(初始化字典)