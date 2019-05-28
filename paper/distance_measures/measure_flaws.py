import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('./../..')
from paper.mydefaults import mydefaults


# Construct time series
noise1 = np.random.randn(20,1)
noise2 = np.random.randn(20,1)
t11 = np.vstack([np.zeros([20,1]), 20+noise1, np.zeros([20,1]), 30+noise2, np.zeros([20,1])])
t12 = np.vstack([np.zeros([20,1]), 25+noise1, np.zeros([20,1]), 25+noise2, np.zeros([20,1])])

t21 = np.vstack([np.zeros([37,1]), np.ones([6,1]), np.zeros([12,1]), np.ones([6,1]), np.zeros([39,1])])
t22 = np.vstack([np.zeros([29,1]), np.ones([6,1]), np.zeros([32,1]), np.ones([6,1]), np.zeros([27,1])])


# Normalise
t11 = t11 - np.mean(t11)
t11 /= np.std(t11, ddof=1)
t12 = t12 - np.mean(t12)
t12 /= np.std(t12, ddof=1)
t21 = t21 - np.mean(t21)
t21 /= np.std(t21, ddof=1)
t22 = t22 - np.mean(t22)
t22 /= np.std(t22, ddof=1)

# workaround bug where plots had different font size
fig, ax = plt.subplots(1, 1)
fig, ax = mydefaults(fig, ax, r=0.4)

fig, ax = plt.subplots(1, 1)
fig, ax = mydefaults(fig, ax, r=0.4)
ax.axis([0, 100, -1, 3.5])
ax.plot(t21)
ax.plot(t22)
ax.plot([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('shift_in_time.pdf')

fig, ax = plt.subplots(1, 1)
fig, ax = mydefaults(fig, ax, r=0.4)
ax.axis([0, 100, -1, 3.5])
ax.plot(t11)
ax.plot(t12)
ax.plot([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('shift_in_value.pdf')
