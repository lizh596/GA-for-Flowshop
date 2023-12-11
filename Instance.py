
# 时  间：2023/9/22 21:19
import random
random.seed(32)  # 随机种子

'''  随机实例--原代码
n 个工件要在 m 台机器上加工，每个工件需要经过 m 道工序，
每道工序要求不同的机器，n 个工件在 m 台机器上的加工顺序相同。工件在机器上的加工时间是给定的(每个工件的工序时间不同)。'''
# State:工序数，即工件有几道工序，Job:工件数，Machine['type':list],对应各工序的并行机数量
def Generate(State, Job, Machine):  # 生成随机实例
    PT = []    # 实例列表
    for i in range(State):
        Si = []       # 每道工序的所有并行机的所有工件的加工时间列表
        for j in range(Machine[i]):  # 遍历每道工序的并行机数量
            S0 = [random.randint(1,20) for k in range(Job)]  # 随机生成每个工件在特定机器上加工时间（多余很多无效时间）
            Si.append(S0)
        PT.append(Si)
    print(S0)  # 最后一道工序对应的第二个并行机的所有工件的加工时间
    print(Si)  # 最后一道工序对应的所有并行机的所有工件的加工时间
    print(PT)  # 每道工序对应的所有并行机的所有工件的加工时间
    #  在这个列表中，PT[i][j][k]表示第i道工序的第j个并行机的第k个工件的加工时间
    # 每个元素代表一道工序

    return PT  # PT （processing time）

Job = 8  # 工件数
State = 5  # 工序数
Machine = [3, 3, 2, 3, 3]  # 每个工序的并行机数量   流水车间工序数相同

PT = Generate(State, Job, Machine)