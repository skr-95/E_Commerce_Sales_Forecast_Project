from sklearn.model_selection import GridSearchCV
from sklearn import metrics


class ModelFit:

    def __init__(self, clf, params=None):
        if params:
            self.clf = clf(**params)
        else:
            self.clf = clf()

    def train(self, X_train, Y_train):
        self.clf.fit(X_train, Y_train)

    def predict(self, X):
        return self.clf.predict(X)

    def grid_train(self, param_grid, k):
        self.grid = GridSearchCV(estimator=self.clf, param_grid=param_grid, cv=k)

    def grid_fit(self, X_train, Y_train):
        self.grid.fit(X_train, Y_train)

    def grid_predict(self, X_test, Y_test):
        self.predictions = self.grid.predict(X_test)
        print("正确率: {:.2f} %".format(100 * metrics.accuracy_score(Y_test, self.predictions)))
