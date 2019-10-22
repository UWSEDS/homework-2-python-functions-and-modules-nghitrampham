import urllib

# link = "https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.csv?accessType=DOWNLOAD"
link = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)


def create_test_dataframe(df, list_cols):
    cond1 = (list(df.columns) == list_cols)
    cond2 = [df[x].map(type).nunique() -1 for x in df.columns]
    cond3 = df.shape[0] > 10
    
    if cond1 and cond2 and cond3:
        return True 
    else:
        return False