import numpy as np
from scipy.stats import skew, kurtosis


def get_stat_data(raw_list: list[int]):
    np_list = np.array(raw_list, dtype=np.float64)

    value_min = np_list.min()
    value_max = np_list.max()
    value_range = value_max - value_min
    value_median = np.median(np_list)
    value_sum = np_list.sum()
    value_mean = np_list.mean()
    value_var = np.var(np_list)
    value_std = np_list.std()
    value_skew = skew(np_list)
    value_kurt = kurtosis(np_list)

    return {
        'min': value_min,
        'max': value_max,
        'range': value_range,
        'median': value_median,
        'sum': value_sum,
        'mean': value_mean,
        'var': value_var,
        'std': value_std,
        'skew': value_skew,
        'kurt': value_kurt,
    }
