import matplotlib.pyplot as plt
import matplotlib.animation as anim
import pandas as pd
from matplotlib import style

style.use("fivethirtyeight")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):

    graph_data = pd.read_csv("Animation_Test.csv")

    x = list(graph_data["X1"])[-20:]
    y = list(graph_data["Y1"])[-20:]
    y2 = list(graph_data["Y2"])[-20:]
    ax1.clear()
    ax1.plot(x, y)
    ax1.plot(x, y2)

ani = anim.FuncAnimation(fig, animate, interval=1000)
plt.show()

