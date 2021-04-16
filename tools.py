from scipy.stats import skewnorm
import numpy as np

def get_statistics(df):
    flat = np.concatenate(df['norm']).ravel()

    flat = flat[~np.isnan(flat)]

    a, loc, scale = skewnorm.fit(flat)

    stats = np.linalg.lstsq(np.array(df['mean'])[:, np.newaxis], df['std'])[0][0]

    return_dict = {'a': a,
                   'loc': loc,
                   'scale': scale,
                   'stats': stats,
                   'n': len(flat)}

    return return_dict


def get_std_from_mean(mean_depth, grad):
    std = mean_depth * grad
    return (std)


def depth_distribution_from_depth(mean_depth, dep_bin_edges, statistics):
    dep_bin_centres = dep_bin_edges[:-1] + (dep_bin_edges[1] - dep_bin_edges[0]) / 2

    std = get_std_from_mean(mean_depth, statistics['stats'])

    std_bin_edges = (dep_bin_edges - mean_depth) / std
    std_bin_centres = std_bin_edges[:-1] + (std_bin_edges[1] - std_bin_edges[0]) / 2
    std_bw = np.nanmean(np.diff(std_bin_edges))

    fit = skewnorm.pdf(std_bin_centres,
                       statistics['a'],
                       statistics['loc'],
                       statistics['scale']) * std_bw

    return (dep_bin_centres, fit)