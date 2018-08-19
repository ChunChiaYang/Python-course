import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams['font.sans-serif']=['SimHei']

#開檔取得資料
with open('multiTimeline2.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    data=[row for row in  reader]

rbc=[int(row[1]) for row in data]
platelet=[int(row[2]) for row in data]

#設定圖表
fig = plt.figure()
ax = plt.axes()
ax.set_xlim(0, 30)
ax.set_ylim(0, 100)

line, = plt.plot([], [])
line1, =plt.plot([],[], color='r')

#初始函式
def init():
    line.set_data([], [])
    line1.set_data([], [])
    return line,line1

#更新函式
def update(frame):
    x=[i for i in range(frame+1)]
    ydata=rbc[:frame+1]
    y1data=platelet[:frame+1]
    
    line.set_data(x,ydata)
    line1.set_data(x,y1data)
    return line,line1


ani = FuncAnimation(fig, update, frames=len(data),
                    init_func=init)

plt.title('近一個月紅血球和血小板的搜尋熱度(台灣)')
plt.ylabel('搜尋熱度',rotation=0)
plt.xlabel('天數')
plt.legend((line,line1),('紅血球','血小板'))
plt.grid()
plt.show()