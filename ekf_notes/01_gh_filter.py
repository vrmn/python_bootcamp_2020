import numpy as np
import matplotlib.pyplot as plt


# fig = plt.figure()
# x = np.arange(10)
# y = 2.5 * np.sin(x / 20 * np.pi)
# yerr = np.linspace(0.05, 0.2, 10)
#
# plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
#
# plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
#
# plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
#              label='uplims=True, lolims=True')
#
# upperlimits = [True, False] * 5
# lowerlimits = [False, True] * 5
# plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
#              label='subsets of uplims and lolims')
#
# plt.legend(loc='lower right')
#
# plt.show()


fig = plt.figure(figsize=(11,1.5))

# x = [160]
# y = []
# xerror1 = 3
plt.xlim(150, 180)
plt.ylim(-1,1)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.errorbar(160, 0, xerr=3, fmt='o', label='A', capthick=2, capsize=10)
plt.errorbar(170, 0.2, xerr=9, fmt='o', label='B', capthick=2, capsize=10)
plt.gca().axes.yaxis.set_ticks([])
plt.show()
