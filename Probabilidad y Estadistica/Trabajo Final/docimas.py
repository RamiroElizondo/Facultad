import numpy as np
from scipy.stats import ttest_1samp, norm

class Docima:
    def __init__(self):
        pass

    def docima_media_varianza_conocida(self, sample, mu_0, sigma):
        n = len(sample)
        media_muestral = np.mean(sample)
        z = (media_muestral - mu_0) / (sigma / np.sqrt(n))
        p = 2 * (1 - norm.cdf(abs(z)))
        return z, p

    def docima_media_varianza_desconocida(self, sample, mu_0):
        t_stat, p_value = ttest_1samp(sample, mu_0)
        return t_stat, p_value

    def docima_media_varianza_desconocida(self, sample, mu_0):
        t_stat, p_value = ttest_1samp(sample, mu_0)
        return t_stat, p_value
    
    

