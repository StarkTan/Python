import pandas as pd
import numpy as np


def create_data():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    dates = pd.date_range('20170101', periods=7)
    print(dates)
    print("--" * 16)
    df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
    print(df)
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20170102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)


def view_data():
    import pandas as pd
    import numpy as np

    dates = pd.date_range('20170101', periods=7)
    df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
    print(df.head(2))
    print("--------------" * 10)
    print(df.tail(3))

    print("index is :")
    print(df.index)
    print("columns is :")
    print(df.columns)
    print("values is :")
    print(df.values)

    print(df.describe())

    print(df.T)

    print(df.sort_index(axis=1, ascending=False))

    print(df.sort_values(by='B'))


def slice_data():
    dates = pd.date_range('20170101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print(df['A'])

    print(df[0:3])
    print("========= 指定选择日期 ========")
    print(df['20170102':'20170103'])

    print(df.loc[dates[0]])

    print(df.loc[:, ['A', 'B']])
    print(df.loc['20170102':'20170104', ['A', 'B']])
    print(df.loc['20170102', ['A', 'B']])
    print(df.loc[dates[0], 'A'])
    print(df.at[dates[0], 'A'])
    print(df.iloc[3])
    print(df.iloc[3:5, 0:2])
    print(df.iloc[[1, 2, 4], [0, 2]])
    print(df.iloc[1:3, :])
    print(df.iloc[:, 1:3])
    print(df.iloc[1, 1])
    print(df[df.A > 0])
    print(df[df > 0])
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

    print(df2)

    print("============= start to filter =============== ")

    print(df2[df2['E'].isin(['two', 'four'])])


# create_data()
# view_data()
slice_data()
