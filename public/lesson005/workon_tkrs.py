#codeing utf-8
"""
workon_tkrs.py

This script should help workon_tkrs.bash "work-on" tkrs from GCP Pub/Sub.

Demo:
python workon_tkrs.py
"""

import subprocess as sp
import re

cmd_s = 'gcloud pubsub subscriptions pull --auto-ack sub10 --project pubsub-197323'
out_s = sp.run(cmd_s, shell=True, stdout=sp.PIPE)

"""
I should match something like this:
┌─────────────────────────┬────────────────┬────────────┐
│           DATA          │   MESSAGE_ID   │ ATTRIBUTES │
├─────────────────────────┼────────────────┼────────────┤
│ Please work on AAPL now │ 55903378213755 │            │
└─────────────────────────┴────────────────┴────────────┘
"""

out_l = out_s.stdout.decode('utf-8').split()
tkr_i = 1+out_l.index('on') # exception ok here
print('tkr:')
print(out_l[tkr_i])

'bye'
