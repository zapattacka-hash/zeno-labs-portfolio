import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Sample data for your tracker
plt.plot([1, 2, 3], [4, 5, 6], label='Variant Alpha')
plt.title('Zeno Labs - Matplotlib Test')
plt.xlabel('Time')
plt.ylabel('Activity')
plt.legend()

plt.savefig('test_plot.png')
print("Plot saved as test_plot.png")
