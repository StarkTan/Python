import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_json('data.json', dtype=np.str)
df = df.sort_values(by=["trade_date"], ascending=True)


def mount_bar(df):
    df = df[df.trade_date > '20190101']
    # dates = pd.to_datetime(df['trade_date'])
    dates = df['trade_date']
    print(dates)
    mounts = pd.to_numeric(df['amount'])
    fig, axes = plt.subplots(figsize=(12, 3))
    axes.bar(dates, mounts, align="center", width=0.7, alpha=1)
    x_labels = axes.get_xticklabels()
    for label in x_labels:
        label.set_visible(False)
    for label in x_labels[::20]:
        label.set_visible(True)
    plt.show()


mount_bar(df)
