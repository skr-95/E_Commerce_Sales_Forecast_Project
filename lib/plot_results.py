import matplotlib.pyplot as plt
import numpy as np
import itertools
import os
from sklearn.metrics import confusion_matrix
from matplotlib.font_manager import FontProperties
from sklearn.model_selection import learning_curve
from wordcloud import WordCloud
import matplotlib.patches as mpatches
import seaborn as sns
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)


def plot_confusion_matrix(Y_test, Y_pred, n_cluster, normalize=False, title='混淆矩阵', model_name=''):
    classes = [i for i in range(n_cluster)]
    cnf_matrix = confusion_matrix(Y_test, Y_pred)
    np.set_printoptions(precision=2)

    if normalize:
        cnf_matrix = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
        print("标准化的矩阵")
    else:
        print('没有标准化的混淆矩阵')

    if model_name:
        title = model_name + "的" + title

    plt.imshow(cnf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(title, fontproperties=font_set)
    plt.colorbar()
    tick_marks = np.arange(n_cluster)
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cnf_matrix.max() / 2.
    for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
        plt.text(j, i, format(cnf_matrix[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cnf_matrix[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('真实值', fontproperties=font_set)
    plt.xlabel('预测值', fontproperties=font_set)

    path = os.getcwd() + "\\fig\\" + model_name + "_cnf_matrix"
    if not os.path.exists(path):
        plt.savefig(path, dpi=500, bbox_inches='tight')


def summary_confusion_matrices(Y_test, Y_pred_list, n_cluster, model_names):
    def make_cnf_matrix(Y_test, Y_pred, n_cluster, increment, normalize=False,
                        title='混淆矩阵', model_name=''):
        if model_name:
            title = model_name + "的" + title
        classes = [i for i in range(n_cluster)]
        cnf_matrix = confusion_matrix(Y_test, Y_pred)
        np.set_printoptions(precision=2)

        ax1 = fig.add_subplot(4, 3, increment)
        ax1.imshow(cnf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(title, fontproperties=font_set, fontsize=20)
        # ax1.colorbar()
        tick_marks = np.arange(n_cluster)
        plt.xticks(tick_marks, classes, rotation=0)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cnf_matrix.max() / 2.
        for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
            plt.text(j, i, format(cnf_matrix[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cnf_matrix[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('真实值', fontproperties=font_set, fontsize=12)
        plt.xlabel('预测值', fontproperties=font_set, fontsize=12)

    n_models = len(Y_pred_list)
    fig = plt.figure(1, figsize=(14, 20))
    for i in range(n_models):
        make_cnf_matrix(Y_test, Y_pred_list[i], n_cluster, model_name="{}".format(model_names[i]), increment=i + 1)

    path = os.getcwd() + "\\fig\\" + "cnf_matrix_summary"
    if not os.path.exists(path):
        plt.savefig(path, dpi=500, bbox_inches='tight')



def plot_learning_curve(estimator, X, y, ylim=None, cv=None,
                        n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 10),
                        title="学习曲线", model_name=""):
    """Generate a simple plot of the test and training learning curve"""

    if model_name:
        title = model_name + "的" + title

    plt.figure()
    plt.title(title, fontproperties=font_set)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("训练实例", fontproperties=font_set)
    plt.ylabel("得分", fontproperties=font_set)
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

    plt.legend(loc="best")

    path = os.getcwd() + "\\fig\\" + model_name + "_learning_curve"
    if not os.path.exists(path):
        plt.savefig(path, dpi=500, bbox_inches='tight')

    return plt


def plot_wordcloud(occurence, n_cluster):
    def random_color_func(self, word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):
        h = int(360.0 * tone / 255.0)
        s = int(100.0 * 255.0 / 255.0)
        l = int(100.0 * float(random_state.randint(70, 120)) / 255.0)
        return "hsl({}, {}%, {}%)".format(h, s, l)

    def make_wordcloud(liste, increment):
        ax1 = fig.add_subplot(4, 2, increment)
        words = dict()
        trunc_occurences = liste[0:150]
        for s in trunc_occurences:
            words[s[0]] = s[1]
        wordcloud = WordCloud(width=1000, height=400, background_color='lightgrey',
                              max_words=1628, relative_scaling=1,
                              color_func=random_color_func,
                              normalize_plurals=False)
        wordcloud.generate_from_frequencies(words)
        ax1.imshow(wordcloud, interpolation="bilinear")
        ax1.axis('off')
        plt.title('cluster nº{}'.format(increment - 1))

    fig = plt.figure(1, figsize=(14, 14))
    color = [0, 160, 130, 95, 280, 40, 330, 110, 25]
    for i in range(n_cluster):
        list_cluster_occurences = occurence[i]

        tone = color[i]  # define the color of the words
        liste = []
        for key, value in list_cluster_occurences.items():
            liste.append([key, value])
        liste.sort(key=lambda x: x[1], reverse=True)
        make_wordcloud(liste, i + 1)

    path = "./fig/word_cloud"
    if not os.path.exists(path):
        plt.savefig(path, dpi=500, bbox_inches='tight')


def plot_PCA_relation(mat, n_cluster):
    sns.set_style("white")
    sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 2.5})

    LABEL_COLOR_MAP = {0: 'r', 1: 'tan', 2: 'b', 3: 'k', 4: 'c', 5: 'g', 6: 'deeppink', 7: 'skyblue', 8: 'darkcyan',
                       9: 'orange',
                       10: 'yellow', 11: 'tomato', 12: 'seagreen', 13: "#9b59b6", 14: "#3498db"}
    label_color = [LABEL_COLOR_MAP[l] for l in mat['cluster']]

    fig = plt.figure(figsize=(12, 10))
    increment = 0
    for ix in range(6):
        for iy in range(ix + 1, 6):
            increment += 1
            ax = fig.add_subplot(4, 3, increment)
            ax.scatter(mat[ix], mat[iy], c=label_color, alpha=0.5)
            plt.ylabel('PCA {}'.format(iy + 1), fontsize=12)
            plt.xlabel('PCA {}'.format(ix + 1), fontsize=12)
            ax.yaxis.grid(color='lightgray', linestyle=':')
            ax.xaxis.grid(color='lightgray', linestyle=':')
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)

            if increment == 12: break
        if increment == 12: break

    comp_handler = []
    for i in range(n_cluster):
        comp_handler.append(mpatches.Patch(color=LABEL_COLOR_MAP[i], label=i))

    plt.legend(handles=comp_handler, bbox_to_anchor=(1.1, 0.9),
               title='Cluster', facecolor='lightgrey',
               shadow=True, frameon=True, framealpha=1,
               fontsize=13, bbox_transform=plt.gcf().transFigure)

    plt.tight_layout()

    path = "./fig/customer_PCA_relation"
    if not os.path.exists(path):
        plt.savefig(path, dpi=500, bbox_inches='tight')