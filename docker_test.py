# docker_test.py

import pandas as pd
import seaborn as sns

# load the tips dataset
tips_df = sns.load_dataset("tips")

#
print(tips_df.head())