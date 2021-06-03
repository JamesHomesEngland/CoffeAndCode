import pandas as pd

df = pd.read_csv(r"C:\Users\James.Hinkley\OneDrive - Homes England\Documents\Projects\Geoadressing\CoffeAndCode\LR_to_PQI.csv")
uprnAdd = df
for index, row in df.iterrows():
    actAdds = [row.iloc[0]["building_name"],
               row.iloc[0]["sub_building_name"],
               row.iloc[0]["building_number"],
               row.iloc[0]["thoroughfare"],
               row.iloc[0]["dep_locality"],
               row.iloc[0]["postcode"]]
    print(actAdds)
    #actString2 = makeString(actAdds2)
    # actAdds2 = [row.iloc[0]["sub_building_name"],
    #             row.iloc[0]["building_name"],
    #             row.iloc[0]["building_number"],
    #             row.iloc[0]["thoroughfare"],
    #             row.iloc[0]["dep_locality"],
    #             row.iloc[0]["postcode"]]
    # #actString2 = makeString(actAdds2)
    # actAdds3 = [row.iloc[0]["sub_building_name"],
    #             row.iloc[0]["building_name"],
    #             row.iloc[0]["thoroughfare"],
    #             row.iloc[0]["dep_locality"],
    #             row.iloc[0]["postcode"]]
    # #actString3 = makeString(actAdds3)
    # actAdds4 = [row.iloc[0]["sub_building_name"],
    #             row.iloc[0]["building_name"],
    #             row.iloc[0]["building_number"],
    #             row.iloc[0]["thoroughfare"],
    #             row.iloc[0]["postcode"]]
    # #actString4 = makeString(actAdds4)