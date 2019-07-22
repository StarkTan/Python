import pandas as pd
import numpy as np


def _append():
    """
    DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=None)
    """
    df = pd.DataFrame(np.arange(6).reshape(2, 3), index=[0, 1], columns=list('ABC'))
    print(df)
    df = df.append([{'A': 6, 'B': 7, 'C': 8}])
    print(df)
    df = df.append(pd.Series({'A': 9, 'B': 10, 'C': 11}, name=0), ignore_index=True)
    print(df)
    df['D'] = list("1234")
    print(df)
    return


def _concat():
    """
    pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
    """
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                       index=[0, 1, 2, 3])

    df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                       index=[4, 5, 6, 7])

    df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                       index=[8, 9, 10, 11])
    frames = [df1, df2, df3]
    result = pd.concat(frames)
    print(result)
    result = pd.concat(frames, keys=['x', 'y', 'z'])
    print(result)
    print('-' * 20)
    df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                        'D': ['D2', 'D3', 'D6', 'D7'],
                        'F': ['F2', 'F3', 'F6', 'F7']},
                       index=[2, 3, 6, 7])
    result = pd.concat([df1, df4], axis=1)
    print(result)
    print('*' * 40)
    result = pd.concat([df1, df4], axis=1, join='inner')  # 取交集
    print(result)
    result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
    print(result)


def _join():
    """
    join(self, other, on=None, how='left', lsuffix='', rsuffix='',
             sort=False):
    """
    df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                       'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
    other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                          'B': ['B0', 'B1', 'B2']})
    print(df.join(other, lsuffix='_caller', rsuffix='_other'))  # 为重复 column 添加前缀
    print(df.set_index('key').join(other.set_index('key')))
    print(df.join(other.set_index('key'), on='key', how='right'))  # left,right表示以哪边的index为准
    print(df.join(other.set_index('key'), on='key', how='inner'))  # inner,outer 表示交集、并集


def _merge():
    """
    merge(self, right, how='inner', on=None, left_on=None, right_on=None,
              left_index=False, right_index=False, sort=False,
              suffixes=('_x', '_y'), copy=True, indicator=False,
              validate=None):
    """
    df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                        'value': [1, 2, 3, 5]})
    df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                        'value': [5, 6, 7, 8]})
    print(df1)
    print(df2)
    print(df1.merge(df2, left_on='lkey', right_on='rkey'))
    print(df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right')))


# _append()
# _concat()
# _join()
_merge()
