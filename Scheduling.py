
# 时  间：2023/9/22 21:20
import random
import matplotlib.pyplot as plt
import numpy as np

class Item:  # 物体
    def __init__(self):  # 初始化
        self.start = []
        self.end = []
        self._on = []
        self.T = []
        self.last_ot = 0
        self.L = 0

    def update(self, s, e, on, t):  # 更新
        self.start.append(s)  # s：开始时间
        self.end.append(e)
        self._on.append(on)  #
        self.T.append(t)
        self.last_ot = e
        self.L += t

class Scheduling:
    def __init__(self, J_num, Machine, State, PT):  # 初始化
        self.M = Machine
        self.J_num = J_num
        self.State = State
        self.PT = PT
        self.Create_Job()
        self.Create_Machine()
        self.fitness = 0

    def Create_Job(self):  # 生成工件列表
        self.Jobs = []
        for i in range(self.J_num):  # 每个工件
            J = Item()
            self.Jobs.append(J)


    def Create_Machine(self):  # 生成机器
        self.Machines = []
        for i in range(len(self.M)):    # len(M):工序数 i:：第几道工序
            State_i = []  # State_i：第i道工序对应的机器列表
            for j in self.M[i]:  # j：机器   第i道工序对应的机器
                M = Item()  # 给机器赋予初始值
                State_i.append(M)
            self.Machines.append(State_i)  # 包含每道工序对应的机器（带有特征的机器）列表

    #每个阶段的解码
    def Stage_Decode(self, CHS, Stage):  # 每个工序的解码 CHS：染色体  Stage：第几道工序
        for i in CHS:  # i：工件
            last_od = self.Jobs[i].last_ot
            last_Md = [self.Machines[Stage][M_i].last_ot for M_i in range(len(self.M[Stage]))]  # 机器的完成时间
            last_ML = [self.Machines[Stage][M_i].L for M_i in range(len(self.M[Stage]))]  # 机器的总负载 M_i：机器索引
            M_time = []    # M_time：当前工序在所有并行机器的加工时间
            for j in self.M[Stage]:  # 遍历当前工序的机器 j：并行机器编号
                time = self.PT[Stage][j][i]
                M_time.append(time)

            #M_time = [self.PT[Stage][M_i][i] for M_i in range(self.M[Stage])]    # 机器对当前工序的加工时间
            # PT[Stage][M][i] ：工序Stage的机器M在第i道工序的加工时间   # M = Machine M[Stage]:当前工序的并行机数
            O_et = [last_Md[_]+M_time[_] for _ in range(len(self.M[Stage]))]  # O_et：机器完成时间
            if O_et.count(min(O_et)) > 1 and last_ML.count(last_ML) > 1:  # 完成时间和机器负载都相同时
                #Machine = random.randint(0, self.M[Stage])
                Machine = random.randint(0, len(self.M[Stage])-1)  # 随机选择一个机器的索引
            elif O_et.count(min(O_et)) > 1 and last_ML.count(last_ML) < 1:  # 完成时间相同而负载不相同时
                Machine = last_ML.index(min(last_ML))  # 选择负载最小的机器
            else:
                Machine = O_et.index(min(O_et))
            s, e, t = max(last_od, last_Md[Machine]), max(last_od, last_Md[Machine])+M_time[Machine], M_time[Machine]
            self.Jobs[i].update(s, e, Machine, t)  # 更新
            self.Machines[Stage][Machine].update(s, e, i, t)  # 更新
            if e > self.fitness:
                self.fitness = e

    #解码
    def Decode(self, CHS):  # 解码  CHS：染色体
        for i in range(self.State):  # i：第几道工序  self.State：工序数
            self.Stage_Decode(CHS, i)
            Job_end = [self.Jobs[i].last_ot for i in range(self.J_num)]  # 每个工件的完成时间
            CHS = sorted(range(len(Job_end)), key=lambda k: Job_end[k], reverse=False)  # 按照工件的完成时间排序
    '''这行代码的作用是对 Job_end 列表的索引进行排序，排序的关键字是 Job_end 中的值，排序方式为升序（因为 reverse=False）。
range(len(Job_end)) 生成一个与 Job_end 列表长度相同的索引序列。
key=lambda k: Job_end[k] 定义了排序的关键字，这里的关键字是 Job_end 中的对应索引的值，即工作完成时间。
reverse=False 指定了排序方式为升序。
最后的结果 CHS 是一个列表，列表的元素是 Job_end 列表中元素的索引，这些索引按照 Job_end 中对应元素的值（即工作完成时间）进行升序排序。
'''
# 画甘特图
    def Gantt(self):
        fig = plt.figure()
        M = ['red', 'blue', 'yellow', 'orange', 'green', 'moccasin', 'purple', 'pink',  'Thistle',
             'Magenta', 'SlateBlue', 'RoyalBlue', 'Aqua', 'floralwhite', 'ghostwhite', 'goldenrod', 'mediumslateblue',
             'navajowhite','navy', 'sandybrown']
        M_num = 0
        for i in range(len(self.M)):  # 遍历工序 self.M:Machine  给每个机器行赋值
            for j in range(len(self.M[i])):  # 遍历并行机器  self.M[i]:第i道工序的机器列表  给并行机分别赋值
                for k in range(len(self.Machines[i][j].start)):  # 遍历每道工序的每个机器  self.Machines[i][j]:第i道工序的第j个机器
                    Start_time = self.Machines[i][j].start[k]
                    End_time = self.Machines[i][j].end[k]
                    Job = self.Machines[i][j]._on[k]  # 第i道工序的第j个机器上的第k个工件
                    plt.barh(M_num, width=End_time - Start_time, height=0.8, left=Start_time,
                             color=M[Job], edgecolor='black')  # 画柱状图
                    plt.text(x=Start_time + ((End_time - Start_time) / 2 - 0.25), y=M_num - 0.2,
                             s=Job+1, size=15, fontproperties='Times New Roman')
                M_num += 1
        plt.yticks(np.arange(M_num + 1), np.arange(1, M_num + 2), size=20, fontproperties='Times New Roman')  # 设置刻度

        plt.ylabel("机器", size=20, fontproperties='SimSun')
        plt.xlabel("时间", size=10, fontproperties='SimSun')
        plt.tick_params(labelsize=20)  # 设置刻度字体大小
        plt.tick_params(direction='in')  # 设置刻度字体方向
        plt.show()
#
# Sch=Scheduling(J_num,Machine,State,PT)