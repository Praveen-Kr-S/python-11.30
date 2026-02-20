#Packages
import webbrowser as wb
# wb.open("https://livewiresalem.com/")
# wb.open_new_tab("https://livewiresalem.com/")


import numpy as np

# l = [10,20,30,40,50,60]
# print(l,type(l))
# ar1 = np.array(l)
# print(ar1, type(ar1))
# print(ar1[1])
# print(ar1[1:3])
# print(ar1.min())
# print(ar1.max())
# print(ar1.sum())
# print(ar1.mean())
# print(np.shape(ar1))
# print(np.power(ar1,2))
# print(np.sqrt(ar1))
# ar = np.array([1.1,2.3,4.6])
# print(np.ceil(ar))
# print(np.floor(ar))
# ar2 = np.array([1,2,3,4,5,6])
# print(ar1+ar2)
# print(ar1-ar2)
#
# mr = np.array([[1,2,3],[4,5,6]])
# print(mr)
# print(mr[1])
# print(mr[1][2])
# print(mr.reshape((3,2)))


import pandas as pd
# vs_data = pd.read_csv(r"C:\Users\Livewire\Desktop\table_chart_datas.csv")
# print(vs_data)
# sales = vs_data["Max of Sales"].values
# print(sales.sum())

info = {
    "Name" : ["Anusha","Stephen","Vishnu Priya","Vidhya","Thani Arasan"],
    "Course":["Python","Java","Django","React.js","Angluar.js"],
    "LPA":[500000,600000,700000,800000,900000]
}

# df = pd.DataFrame(info)
# print(df)
# print(df.head(2))
# print(df.tail(2))

import matplotlib.pyplot as plt
Region = ["South","Centrel","North","East"]
Sales = [200000,300000,800000,500000]
plt.title("Sales of each Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.bar(Region,Sales)
plt.show()




