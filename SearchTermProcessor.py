report_path = "d:\Downloads\search-term-report-2017-01-16-52396017242.txt"

class report_row:
    def __init__(self, string):
        data = string.split("\t")

        self.Campaign_Name = data[0]
        self.Ad_Group_Name = data[1]
        self.Customer_Search_Term = data[2]
        self.Keyword = data[3]
        self.Match_Type = data[4]
        self.First_Day_of_Impression = data[5]
        self.Last_Day_of_Impression = data[6]
        self.Impressions = data[7]
        self.Clicks = data[8]
        self.CTR = data[9]
        self.Total_Spend = float(data[10])
        self.Average_CPC = data[11]
        self.ACoS = float(data[12].strip("%"))
        self.Currency = data[13]
        self.Orders_placed = int(data[14])
        self.Product_Sales = float(data[15])
        self.Conversion_Rate = data[16]
        self.Same_SKU_units_Ordered = data[17]
        self.Other_SKU_units_Ordered = data[18]
        self.Same_SKU_units_Product_Sales = data[19]
        self.Other_SKU_units_Product_Sales = data[20]

all_rows = []
with open(report_path) as f:
    f.readline()
    for l in f.readlines():
        all_rows.append(report_row(l))

def filter_rows(all_rows):
    out = []
    for r in all_rows:
        if r.ACoS < 30.0 and r.ACoS > 0:
            out.append(r)
    return out

filtered = filter_rows(all_rows)

sorted_filtered = sorted(filtered, key=lambda x: x.ACoS, reverse=True)

for r in sorted_filtered:
    print("ACoS: {:<5}\tOrders: {:<5}\tCTR: {:<10}\t{}".format(r.ACoS, r.Orders_placed, r.CTR, r.Customer_Search_Term))

spend = 0
sales = 0
for r in all_rows:
    spend = spend + r.Total_Spend
    sales = sales + r.Product_Sales
print("Spend:{:<15} Sales:{:<15} SalesPer$:{:<15}".format(spend, sales, sales/spend))