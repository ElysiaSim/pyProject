import pandas as pd
# Install 'python3 -m pip install --user xlrd'
data = pd.read_excel("dataNew.xls")
data['Period'] = data['Period'].str.replace('Jan', '')
#df = data[(data["Period"] >= 1900) & (data["Period"] <= 1930)]
print(data)
