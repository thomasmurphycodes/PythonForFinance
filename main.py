import fxcmpy
import time
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import pylab
from pylab import plt, mpl

api = fxcmpy.fxcmpy(access_token='1787dbb385a48cf9b67e92e4b2bda2bee3664d40', log_level='error')
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
print('no fail')