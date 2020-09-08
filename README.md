# E-Commerce Sales Forecast

这个项目数据来源自于Kaggle平台上的E-Commerce data.

注：链接是https://www.kaggle.com/carrie1/ecommerce-data

# 1. 项目简介
## 1.1 数据来源
该数据源是来自一家英国网上销售商，是在2010年1月12日至2011年9月12日之间产生的50万条销售数据。销售的商品主要为一次性礼物，购买用户主要为各地的批发商。

## 1.2 项目目的
**目的: 构建再次购买可能性指标, 利用该指标, 提高用户复购率, 增加企业利润**

## 1.3 数据说明
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/original_data_info.png" width="900" height="255" />

> *InvoiceNo*: 每一笔订单的单号

> *StockCode*: 订单中的一种商品编号

> *Description*: 对这种商品的描述

> *Quantity*: 在这一订单中这种商品的数量

> *InvoiceDate*: 每笔订单的发生时间

> *UnitPrice*: 该商品的单价

> *CustomerID*: 购买者的用户ID

> *Country*: 购买用户的国家

 # 2. 特征工程
 
## 2.1 商品特征构建

### 2.1.1 商品分组

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/word_cloud.png" width="800" />

### 2.1.2 商品特征
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/invoice_info.png" width="900" />


## 2.2 用户特征构建
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_features_info.png" width="900" />

# 3. 部分结果

## 3.1 参数训练


<a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/SVC_learning_curve.png" width="450"/></a><a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/LR_learning_curve.png" width="450"/></a>

## 3.2 模型预测结果

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/cnf_matrix_summary.png" width="800" />


# 4. 其他
## 4.1 EDA阶段

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/description_info.png" width="900"  />

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_purchase_info.png" width="900"  />

## 4.2 词根词性统计
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/words_occurance_info.png" width="450" />
