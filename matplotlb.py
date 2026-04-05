import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Retail_Sales.csv")

x = df["Category"].value_counts()


plt.pie(x, labels=x.index,
       autopct="%1.1f%%",
       shadow=True
       )

plt.title("The Most Selling")


plt.show()
