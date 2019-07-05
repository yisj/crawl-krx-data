import pandas as pd
from datetime import datetime
import os

if not os.path.exists('krx-stock'):
    os.mkdir('krx-stock')

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
'''
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

code_df = code_df[['회사명', '종목코드']]

code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
'''
print(code_df.to_csv())
with open('krx-stock/%s.csv' % datetime.now().isoformat(), 'w') as f:
    f.write(code_df.to_csv())
