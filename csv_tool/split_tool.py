import pandas as pd

src_csv = 'interpolated.csv'
det_csv = 'new.csv'

data = pd.read_csv(src_csv)
new_fd = data.loc[ ::3 , ['filename', 'angle']]
new_fd.to_csv( det_csv, index=False)