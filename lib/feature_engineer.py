import pandas as pd
from IPython.core.display import display
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
from joblib import load, dump


def feature_engineer(df, n_clusters):
    """
    对数据进行特征工程
    :param df: 源数据
    :param n_clusters: 商品分类组数
    :return: 特征矩阵, 最后一列是label
    """

    # 创建用户分组所需特征
    df_customer = df.groupby(by=["CustomerID"], as_index=False).InvoiceNo.count().rename(columns={"InvoiceNo": "count"})
    df_customer.loc[:, ["Total_price", "Cluster_0", "Cluster_1", "Cluster_2", "Cluster_3", "Cluster_4"]] = \
        df.groupby(by=["CustomerID"], as_index=False)[["Total_price", "Cluster_0", "Cluster_1",
                                                       "Cluster_2", "Cluster_3", "Cluster_4"]].sum()
    for i in range(n_clusters):
        col = 'Cluster_{}'.format(i)
        df_customer.loc[:, col] = df_customer.loc[:, col] / df_customer.loc[:, 'Total_price'] * 100

    df_customer.loc[:, ["min", "max", "mean"]] = df.groupby(by=["CustomerID"], as_index=False).Total_price.agg(
        ["min", "max", "mean"]).reset_index(drop=False)

    customer_col = ['count', 'min', 'max', 'mean', 'Cluster_0', 'Cluster_1', 'Cluster_2', 'Cluster_3', 'Cluster_4']
    matrix = df_customer[customer_col].copy(deep=True).values

    # 特征标准化
    scaler = StandardScaler()
    scaler.fit(matrix)
    scaled_matrix = scaler.transform(matrix)

    if not os.path.exists('./temp/kmeans_model.joblib'):
        # 用户聚类分组
        n_clusters = 11
        kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=200)
        kmeans.fit(scaled_matrix)
        clusters_clients = kmeans.predict(scaled_matrix)

        # 打印各组人数
        display(pd.DataFrame(pd.Series(clusters_clients).value_counts(), columns=["客户人数"]).T)
    else:
        kmeans = load("./temp/kmeans_model.joblib")
        clusters_clients = kmeans.predict(scaled_matrix)
        # 打印各组人数
        display(pd.DataFrame(pd.Series(clusters_clients).value_counts(), columns=["客户人数"]).T)

    # 输出带用户ID的用户特征矩阵
    selected_col = ['CustomerID', 'mean', 'Cluster_0', 'Cluster_1', 'Cluster_2', 'Cluster_3', 'Cluster_4']
    selected_customers_features = df_customer[selected_col].copy(deep=True)
    selected_customers_features.loc[:, 'cluster'] = clusters_clients
    return selected_customers_features
