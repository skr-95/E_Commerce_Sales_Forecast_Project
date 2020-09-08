# E-Commerce Sales Forecast

# 1 项目目的及结果
## 目的: 

### 针对商户销售数据信息，构建用户复购率指标，实现针对性策略提高用户复购率，提高销售额，降低营销成本

## 项目结果：
### 指标正确率：
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/result_4.png" width="200" />

### 预测结果统计：
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/result_1.png" width="400" />

### 收益提升预计：
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/result_2.png" width="1000" />

### 成本节约预计：
<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/result_3.png" width="600" />


# 2 数据简介
该数据源是来自一家英国网上销售商，是在2010年1月12日至2011年9月12日之间产生的50万条销售数据。销售的商品主要为一次性礼物，购买用户主要为各地的批发商。

这个项目数据来源自于Kaggle平台上的E-Commerce data. https://www.kaggle.com/carrie1/ecommerce-data

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/original_data_info.png" width="900" />

> *InvoiceNo*: 每一笔订单的单号</br>
> *StockCode*: 订单中的一种商品编号</br>
> *Description*: 对这种商品的描述</br>
> *Quantity*: 在这一订单中这种商品的数量</br>
> *InvoiceDate*: 每笔订单的发生时间</br>
> *UnitPrice*: 该商品的单价</br>
> *CustomerID*: 购买者的用户ID</br>
> *Country*: 购买用户的国家

 # 3 部分过程

## 3.1 商品类别词根统计

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/word_cloud.png" width="800" />

## 3.2 词根词性统计

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/words_occurance_info.png" width="450" />

## 3.3 商品特征汇总

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/invoice_info.png" width="900" />

## 3.4 用户特征汇总

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_features_info.png" width="900" />

## 3.5 参数训练过程

<a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/SVC_learning_curve.png" width="400"/></a><a style="float:left;"><img border=0 src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/LR_learning_curve.png" width="400"/></a>

## 3.6 最佳参数模型预测结果汇总

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/cnf_matrix_summary.png" width="800" />


# 4. 其他
**EDA过程**

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/description_info.png" width="900"  />

<img src="https://github.com/skr-95/E_Commerce_Sales_Forecast_Project/blob/master/fig/customer_purchase_info.png" width="900"  />
