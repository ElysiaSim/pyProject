import pandas as pd
data = pd.read_excel("dataNew.xls")
data[(data["Period"] >= 1900) & (data["Period"] <= 1930)]
print(data)