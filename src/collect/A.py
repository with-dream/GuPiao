import akshare as ak

stock_info_a_code_name_df = ak.stock_info_a_code_name()
ss = set()

for index in stock_info_a_code_name_df.index:
    value = stock_info_a_code_name_df.loc[index]
    code = value.values[0]
    name = value.values[1]
    print(name)
    ss.add(code[:3])

print(ss)
