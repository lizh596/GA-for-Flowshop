
# 时  间：2023/9/22 21:17
import random
import numpy as np
import copy
from Scheduling import Scheduling as Sch
from Instance_2 import Job, State, Machine, PT
import matplotlib.pyplot as plt

'''混合流水车间：加入了并行机'''
'''流水车间：一组功能不同的机床，待加工工件有多道工序，所用工件的加工路线都是相同的，同一道工序的加工时间不同，工序之间有先后顺序约束。'''
class GA:
    def __init__(self, J_num, State, Machine, PT):  # 初始化
        self.State = State
        self.Machine = Machine
        self.PT = PT
        self.J_num = J_num  #
        self.Pm = 0.2  # 变异概率
        self.Pc = 0.9  # 交叉概率
        self.Pop_size = 100  # 种群大小

    # 随机产生染色体
    def RCH(self):  # RCH：染色体
        Chromo = [i for i in range(self.J_num)]  # 编码方式：基于工件排列  0到J_num-1
        random.shuffle(Chromo)
        return Chromo

    # 生成初始种群
    def CHS(self):  # CHS：种群
        CHS = []
        for i in range(self.Pop_size):
            CHS.append(self.RCH())
        return CHS

    #选择
    def Select(self, Fit_value):  # Fit_value：适应度列表
        Fit = []
        for i in range(len(Fit_value)):
            fit = 1 / Fit_value[i]  # 取倒数
            Fit.append(fit)
        Fit = np.array(Fit)
        idx = np.random.choice(np.arange(len(Fit_value)), size=len(Fit_value), replace=True,
                               p=(Fit) / (Fit.sum()))
        return idx  # idx为被选择的个体索引

    # 交叉
    def Crossover(self, CHS1, CHS2):
        T_r = [j for j in range(self.J_num)]
        r = random.randint(2, self.J_num)  # 在区间[1,T0]内产生一个整数r
        random.shuffle(T_r)
        R = T_r[0:r]  # 按照随机数r产生r个互不相等的整数
        # 将父代的染色体复制到子代中去，保持他们的顺序和位置
        H1 = [CHS1[_] for _ in R]
        H2 = [CHS2[_] for _ in R]
        C1 = [_ for _ in CHS1 if _ not in H2]
        C2 = [_ for _ in CHS2 if _ not in H1]
        CHS1, CHS2 = [], []
        k, m = 0, 0
        for i in range(self.J_num):
            if i not in R:
                CHS1.append(C1[k])
                CHS2.append(C2[k])
                k += 1
            else:
                CHS1.append(H2[m])
                CHS2.append(H1[m])
                m += 1
        return CHS1, CHS2

    # 变异
    def Mutation(self, CHS):
        Tr = [i_num for i_num in range(self.J_num)]
        # 机器选择部分
        r = random.randint(1, self.J_num)  # 在变异染色体中选择r个位置
        random.shuffle(Tr)
        T_r = Tr[0:r]
        K=[]
        for i in T_r:
            K.append(CHS[i])
        random.shuffle(K)
        k=0
        for i in T_r:
            CHS[i]=K[k]
            k+=1
        return CHS

    def main(self):
        BF = []  # 最佳适应度
        x = [_ for _ in range(101)]  # 横坐标 迭代数
        C = self.CHS()  # 初始种群
        Fit = []  # 适应度
        for C_i in C:  # C_i：染色体  得到每个染色体的适应度
            s = Sch(self.J_num, self.Machine, self.State, self.PT)  # 初始化一个实例
            s.Decode(C_i)
            Fit.append(s.fitness)
        best_C = None  # 最佳染色体
        best_fit = min(Fit)
        BF.append(best_fit)
        for i in range(100):  # 100：迭代次数
            C_id = self.Select(Fit)  # C_id：被选择的个体索引
            C = [C[_] for _ in C_id]  # C: 选择后的种群
            for Ci in range(len(C)):
                if random.random() < self.Pc:  # Pc：交叉概率
                    _C = [C[Ci]]  # _C：将选择算子的染色体存入列表
                    CHS1, CHS2 = self.Crossover(C[Ci], random.choice(C))
                    _C.extend([CHS1, CHS2])  # _C：将交叉后的染色体增加存入列表
                    Fi = []
                    for ic in _C:  # ic：遍历交叉后的染色体
                        s = Sch(self.J_num, self.Machine, self.State, self.PT)  # 初始化一个实例 s:就是一个实例
                        s.Decode(ic)  # 解码 解码后ic变为一个列表，列表的元素是 Job_end 列表中元素的索引，这些索引按照 Job_end 中对应元素的值（即工作完成时间）进行升序排序。
                        Fi.append(s.fitness)  # s.fitness：每个染色体的适应度
                    C[Ci] = _C[Fi.index(min(Fi))]
                    Fit.append(min(Fi))
                elif random.random() < self.Pm:
                    CHS1 = self.Mutation(C[Ci])
                    C[Ci] = CHS1
            Fit = []
            Sc = []
            for C_i in C:
                s = Sch(self.J_num, self.Machine, self.State, self.PT)
                s.Decode(C_i)
                Sc.append(s)
                Fit.append(s.fitness)
            if min(Fit) < best_fit:
                best_fit = min(Fit)
                best_C = Sc[Fit.index(min(Fit))]
            BF.append(best_fit)  # BF：每次迭代的最佳适应度列表
            if i % 20 == 0:
                print(i, ":", best_fit)
                best_C.Gantt()
            else:
                pass
        plt.plot(x, BF)
        plt.show()


if __name__ == "__main__":
    g = GA(Job, State, Machine, PT)
    g.main()