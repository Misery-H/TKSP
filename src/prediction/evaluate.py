# import numpy as np
# import pandas as pd
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error, r2_score
#
#
# def evaluation(y_test, y_predict):
#     mae = mean_absolute_error(y_test, y_predict)
#     mse = mean_squared_error(y_test, y_predict)
#     rmse = np.sqrt(mean_squared_error(y_test, y_predict))
#     mape = (abs(y_predict - y_test) / y_test).mean().item()
#     r_2 = r2_score(y_test, y_predict)
#     return mae, rmse, mape, r_2
# def diff_evaluation(y_test, y_predict):
#     # print(len(y_predict), len(y_test))
#     # y_test =[i-j for i,j in zip(y_test[1:],y_test[:len(y_test)-1])]
#     # y_predict=[i-j for i,j in zip(y_predict[1:],y_predict[:len(y_predict)-1])]
#     # print(len(y_predict),len(y_test))
#     y_predict=pd.DataFrame(y_predict).diff().dropna()
#     y_test=pd.DataFrame(y_test).diff().dropna()
#     # print(type(y_test))
#     return evaluation(y_test,y_predict)
#
# # mae, rmse, mape, r_2=evaluation(orginal_y_test_pred,orginal_y_test_tensor)
# # print(f"{config.save_path}:MAE={mae},RMSE={rmse},MAPE={mape},R_2={r_2}")
# # mae_, rmse_, mape_, r_2_=diff_evaluation(orginal_y_test_pred,orginal_y_test_tensor)
# # print(f"Diff_1:{config.save_path}:MAE={mae_},RMSE={rmse_},MAPE={mape_},R_2={r_2_}")
#
# t="""3.177123443
# 3.384770723
# 3.562642802
# 3.669729718
# 3.743818474
# 3.792170613
# 3.82449081
# 3.845881605
# 3.860096895
# 3.869527743
# 3.875788816
# 3.8799443
# 3.88270263
# 3.884533466
# 3.885748704
# 3.886555326
# 3.887090727
# 3.887446104
# 3.887681988
# 3.887838558
# 3.887942482
# 3.888011463
# 3.888057249
# """
# pre=np.array([float(i)  for i in t.split()])
# # print(y)
# k="""2.6442
# 2.4078
# 2.996
# 3.1416
# 3.1086
# 3.5274
# 3.6526
# 4.4177
# 4.1065
# 4.7962
# 4.5859
# 4.6703
# 4.1061
# 4.3962
# 5.1349
# 4.8792
# 5.3992
# 5.0736
# 5.1835
# 4.4177
# 4.1061
# 4.9327
# 4.6972
#
# """
# ori=np.array([float(i) for i in k.split()])
# mae, rmse, mape, r_2=evaluation(ori,pre)
# print(f"MAE={mae},RMSE={rmse},MAPE={mape},R_2={r_2}")
# mae_, rmse_, mape_, r_2_=diff_evaluation(ori,pre)
# print(f"MAE={mae_},RMSE={rmse_},MAPE={mape_},R_2={r_2_}")

res="""0.7414	0.7082	0.5958	0.5481	0.4721	0.4042	0.3994
1.396	1.3254	1.0826	1.0067	0.7611	0.5322	0.4729
1.2603	1.1234	0.7749	0.6611	0.5664	0.4965	0.4653
0.9686	0.8528	0.8721	0.7169	0.6072	0.5509	0.4869
0.8196	0.8068	0.6347	0.6775	0.5784	0.5003	0.4563
0.7728	0.7699	0.6737	0.6381	0.5679	0.5407	0.4419
0.8883	0.8908	0.7989	0.6842	0.5884	0.4586	0.4781
1.1001	0.8828	0.7721	0.6911	0.6672	0.5609	0.4599
"""
k=res.split('\n')
k=[i.split() for i in k]
print(k)
for i in k:
    for j in i