# E-Commerce Sales Forecast

**本项目为数据科学类项目, 在NoteBook上进行Python分析和建模, 图表文报告总长10000字，总代码量近1500行，可视化近10余种图**

### Key words: Python, Pandas, NumPy, Sklearn, SVM, LR, KNN, K-Means, NLTK

## 数据描述:

- 该数据集是交易数据, 来源于在英国的一家专营线上的店铺, 主营商品为各种场合的礼物, 主要的客户都是批发商.
- 该数据集是在2010年1月12日至2011年9月12日(20个月)产生的50万销售数据. (link: https://www.kaggle.com/carrie1/ecommerce-data?select=data.csv)

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/original_data_info.png" width="900" />

> *InvoiceNo*: 每一笔订单的单号</br>
> *StockCode*: 订单中的一种商品编号</br>
> *Description*: 对这种商品的描述</br>
> *Quantity*: 在这一订单中这种商品的数量</br>
> *InvoiceDate*: 每笔订单的发生时间</br>
> *UnitPrice*: 该商品的单价</br>
> *CustomerID*: 购买者的用户ID</br>
> *Country*: 购买用户的国家

这些数据已放在data目录下.

## 项目目的

1: 利用商户销售数据, 探索和总结订单信息, 了解用户特征, 建立数据模型, 帮助企业销售;

2: 实践基于Python的NumPy和Pandas的ETL, 数据分析,特征工程, 和Sklearn的机器学习建模.

## 模型:

本模型的重点在特征工程中, 体现在如何从杂而乱的信息中提取出具有代表性的特征. 

* 在对商品的特征工程中, 商品各自分为一类显然会让模型过拟合, 因此这里采用基于NLTK库的词根词性转化, 然后用Sklearn下的K-Means算法聚成5类. 由此得到不同商品的分类信息.

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/invoice_info.png" width="900" />


* 针对用户, 由于特征信息繁多, 先用PCA降维, 再选取合适的特征进行K-Means聚类.

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_features_info.png" width="900" />

* 在建立模型中, 针对商户销售数据信息，构建用户复购率指标, 选取基于投票算法的SVM, LR, knn, 决策树等的集成模型, 并将结果绘制成一张图表进行对比.

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/cnf_matrix_summary.png" width="800" />


## 项目结果：

* 最终模型指标正确率高达83.77%, 在预测集中运用模型结果统计为: 复购率可能性极小的人数为4人, 很小的人数为178人, 可能复购但可以观望的人数为199人.

* 利用该模型针对性提升指数低的用户, 如提升30%的转化率, 销售额将提高118626.67英镑, 即13.04%; 同时, 也可以从普遍促销转为针对性促销, 从而节省促销成本243627.1英镑, 即减少69.28%.

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/result_2.png" width="1000" />

## 其余部分过程

## 3.1 商品类别词根统计

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/word_cloud.png" width="800" />

## 3.2 参数训练过程

<a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/SVC_learning_curve.png" width="400"/></a><a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/LR_learning_curve.png" width="400"/></a>

## 3.3 最佳参数模型预测结果汇总

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/cnf_matrix_summary.png" width="800" />


# 4. 其他
**EDA过程**

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/description_info.png" width="900"  />

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_purchase_info.png" width="900"  />
