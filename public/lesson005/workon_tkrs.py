#codeing utf-8
"""
workon_tkrs.py

This script should help workon_tkrs.bash "work-on" tkrs from GCP Pub/Sub.

Demo:
python workon_tkrs.py
"""

import numpy      as np
import pandas     as pd
import subprocess as sp
PROJECT = 'pubsub-197323'
cmd_s = 'gcloud pubsub subscriptions pull --auto-ack sub10 --project '+PROJECT
out_s = sp.run(cmd_s, shell=True, stdout=sp.PIPE)

"""
I should match something like this:
┌─────────────────────────┬────────────────┬────────────┐
│           DATA          │   MESSAGE_ID   │ ATTRIBUTES │
├─────────────────────────┼────────────────┼────────────┤
│ Please work on AAPL now │ 55903378213755 │            │
└─────────────────────────┴────────────────┴────────────┘
"""
# I should use a list to find the tkr_s:
out_l = out_s.stdout.decode('utf-8').split()
# I should find the index of 'on'.
# The tkr-index is one-plus the on-index:
tkr_i = 1+out_l.index('on') # exception ok here
tkr_s = out_l[tkr_i]
print('tkr:')
print(tkr_s)

# I should use the tkr to get prices:
url_s    = 'https://cs101.herokuapp.com/lesson005/'+tkr_s+'.csv'
price_df = pd.read_csv(url_s)
# I should generate ML-features from prices:
feat0_df         = price_df[['Date','Close']]
feat0_df.columns = ['cdate','cp']
feat1_df = feat0_df.sort_values('cdate')

# I should compute pctlag1 and then get pctlead from it:
feat1_df['pctlag1'] = (100.0 * (feat1_df.cp - feat1_df.cp.shift(1)) / feat1_df.cp).fillna(0)
feat1_df['pctlead'] = feat1_df.pctlag1.shift(-1).fillna(0)
# In ML-terms, I hope that pctlead depends on pctlag1 (and other features).

'bye'
