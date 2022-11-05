import sys
import pandas as pd

df = pd.read_json(sys.argv[1])
tdf = df.transpose()
print(tdf.columns)
tdf.to_csv('reduced_media.csv', sep=',',columns = ["Media Name", "Media Type", "Location", "Contact Page URL"], mode='w', index=False)
