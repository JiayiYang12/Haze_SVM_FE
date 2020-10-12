'''

其它常用分类算法
1.k近邻（kNN）
2.随机森林算法
3.决策树
4.逻辑斯蒂回归
5.朴素贝叶斯

'''



#1 kNN算法

import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


INPUT_PATH = './data_finall/day_data/feature_xg.csv '
data = pd.read_csv(INPUT_PATH)


data = np.array(data)
x, y = np.split(data, (5,), axis=1)
x = x[:, :5]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=10)
for i in range(1,8):

    #k近邻分类，这里选择i个近邻
    knn=neighbors.KNeighborsClassifier(i,weights='uniform')
    #可以使用fit 或者cross_val_score 函数来得到结果
    knn.fit(x_train,y_train)
    y_predict = knn.predict(x_test)
    MSE = mean_squared_error(y_predict, y_test)
    MAE = mean_absolute_error(y_predict, y_test)
    R2 = r2_score(y_predict, y_test)
    print("MSE:%s,MAE:%s,R2:%s" %(MSE,MAE,R2))
    # for cnt in range(2,10):
    #
    #     score=cross_val_score(knn,X,y,cv=cnt,scoring='accuracy')
    #
    #     print("cv="+str(cnt)+'分成'+str(i)+'个近邻的得分为：'+str(np.mean(score)))




'''
#模型2：随机森林算法

#设定随机森林分类模型
from sklearn import ensemble
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

INPUT_PATH = './data_finall/day_data/feature_xg.csv '
data = pd.read_csv(INPUT_PATH)



for i in range(1,20):
    #设定随机森林分类模型
    rf=ensemble.RandomForestClassifier(i)
    #随机森林分类,X,y可以根据你想探究的字段之间的关系进行设置
    features = ['Iws', 'TEMP', 'DEWP', 'Is', 'Ir']
    X = data[features]

    le=LabelEncoder()
    le.fit(data['pm2.5'])
    y=le.transform(data['pm2.5'])
    #评估分类模型性能
    for k in range(2,10):

        score=cross_val_score(rf,X,y,cv=k,scoring='accuracy')
        print("cv="+str(k)+"选用"+str(i)+"个随机森林分类器的结果为"+str(np.mean(score)))
    #随机森林的计算时间和决策树（基分类器）的数量成正比，尝试调整随机森林中的决策树的数量，看看分类的准确率是如何变化的
    #将结果和KNN、DecisionTree分类的结果进行比较，看看你能得出什么结论
'''

'''

#模型3：决策树

from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
#设定X，y值

INPUT_PATH = './data_finall/day_data/feature_xg.csv '
data = pd.read_csv(INPUT_PATH)

features = ['Iws', 'TEMP', 'DEWP', 'Is', 'Ir']
X = data[features]

le=LabelEncoder()
le.fit(data['pm2.5'])
y=le.transform(data['pm2.5'])
#设定模型
dt=tree.DecisionTreeClassifier()
#训练模型，并得到准确率
from sklearn.model_selection import cross_val_score
for i in range(2,10):

    score=cross_val_score(dt,X,y,cv=i,scoring='accuracy')
    print('cv='+str(i)+"决策树分类结果为："+str(np.mean(score)))

'''


'''

# 模型4 逻辑斯蒂回归(打印结果有点问题,待定！)

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


INPUT_PATH = './data_finall/day_data/feature_xg.csv '
data = pd.read_csv(INPUT_PATH)

features = ['Iws', 'TEMP', 'DEWP', 'Is', 'Ir']
X = data[features]

lm=linear_model.LogisticRegression()
#初始化label
le=LabelEncoder()
le.fit(data['pm2.5'])
y=le.transform(data['pm2.5'])


#通过交叉检验，得到分类准确率
#logistic中的scoring参数指定为accuracy
for i in range(2,10):

    scores=cross_val_score(lm,X,y,cv=i,scoring='accuracy')
    print("逻辑斯蒂回归cv：%s,评分：%s" % (i,scores))



'''




'''
#模型5：朴素贝叶斯



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

INPUT_PATH = './data_finall/day_data/feature_xg.csv '
data = pd.read_csv(INPUT_PATH)

features = ['Iws', 'TEMP', 'DEWP', 'Is', 'Ir']
X = data[features]


le=LabelEncoder()
le.fit(data['pm2.5'])
y=le.transform(data['pm2.5'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = GaussianNB()
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("朴素贝叶斯分类器得分："+str(score))

'''




