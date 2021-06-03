import pandas as pd

df = pd.read_csv(r"C:\Users\James.Hinkley\OneDrive - Homes England\Documents\Projects\Geoadressing\CoffeAndCode\CofAndCode.csv")
uprnAdd = df
for index, row in df.iterrows():
    actAdds = [row["building_name"],
               row["sub_building_name"],
               row["building_number"],
               row["thoroughfare"],
               row["dep_locality"],
               row["postcode"]]

    #actString2 = makeString(actAdds2)
    actAdds2 = [row["sub_building_name"],
                row["building_name"],
                row["building_number"],
                row["thoroughfare"],
                row["dep_locality"],
                row["postcode"]]
    #actString2 = makeString(actAdds2)
    actAdds3 = [row["sub_building_name"],
                row["building_name"],
                row["thoroughfare"],
                row["dep_locality"],
                row["postcode"]]
    #actString3 = makeString(actAdds3)
    actAdds4 = [row["sub_building_name"],
                row["building_name"],
                row["building_number"],
                row["thoroughfare"],
                row["postcode"]]
    #actString4 = makeString(actAdds4)
    print(actAdds, "\n", actAdds2, "\n", actAdds3, "\n", actAdds4)
    exit()