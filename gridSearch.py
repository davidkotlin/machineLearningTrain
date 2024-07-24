from sklearn import datasets
from sklearn.linear_model import LogisticRegression
#載入Scikit-learn 库中的标准数据集
iris = datasets.load_iris()
# print(iris)
#data:該数据集 鳶尾花 的150 个样本，每个样本 4 个特征(花萼长度、花萼宽度、花瓣长度、花瓣宽度)
X = iris['data']
#target:鳶尾花的类别(山鸢尾0、变色鸢尾1、维吉尼亚鸢尾2)
y = iris['target']
# print(iris["DESCR"])鸢尾花数据集的描述信息
#邏輯回歸
logit = LogisticRegression(max_iter = 10000)
# print(logit)
# print(logit.get_params())#預設正則化參數1
#用這個邏輯回歸模型來適配鳶尾花的數據與類別
logit.fit(X,y)
# print(logit.fit(X,y))
#評估模型準確度
print(logit.score(X,y))
new_data = [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.7, 1.5], [7.2, 3.6, 6.1, 2.5]]
predictions = logit.predict(new_data)
print("新數據的預測結果: ", predictions, predictions[0], predictions[1], predictions[2])

# 對新數據的預測機率
prediction_probabilities = logit.predict_proba(new_data)
print("新數據的預測機率: \n", prediction_probabilities)
# #設定正則化參數
C=[0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

scores = []
#進行len(C)次正則化參數帶入的模擬，並紀錄每次模擬的準確率
for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))

print(scores)