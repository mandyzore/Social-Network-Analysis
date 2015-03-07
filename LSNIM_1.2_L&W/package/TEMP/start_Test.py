import os
import string
from graph import Basic
from format import MovieFormat
from format import CitationFormat
from algorithm.util import randomy as RP
from algorithm.greedy import old_greedy
from algorithm.lism import LabledInfluenceMaxi
from algorithm.casm import ICM

import networkx as nx
from time import clock as now

def test():
        # g=choose_data('citation')
        # E=g[1]#[eID,nID1,nID2]


        # edgelist=[(E[i][1],E[i][2]) for i in range(200)]
        # print(edgelist)

        # ee=[(0, 1), (1, 3), (2, 4), (4, 5), (5, 3)]
        ##-------------------------------------------
        G=nx.Graph()
        G.add_nodes_from([1,2,3,4,5,6,7,8])
        # networkx draw()
        nx.draw(G)
        # pyplot draw()
        # plt.savefig("citation.png")
        plt.draw()
        print('end')

        ##-------------------------------------------
        import matplotlib.pyplot as plt
        import networkx as nx
        G=nx.dodecahedral_graph()
        nx.draw(G) # networkx draw()
        plt.draw() # pyplot draw()

        
        ##-------------------------------------------
        import networkx as nx                   #导入networkx包
        import matplotlib.pyplot as plt     #导入绘图包matplotlib（需要安装，方法见第一篇笔记）

        G =nx.random_graphs.barabasi_albert_graph(100,1)   #生成一个BA无标度网络G
        print(len(G))
        nx.draw(G)                          #绘制网络G
        # plt.savefig("ba.png")           #输出方式1: 将图像存为一个png格式的图片文件
        plt.show()                            #输出方式2: 在窗口中显示这幅图像

        ##-------------------------------------------
        import networkx as nx
        import matplotlib.pyplot as plt

        g=choose_data('citation')
        E=g[1]#[eID,nID1,nID2]
        V=g[0]
        edgelist=[(i[1],i[2]) for i in E]

        G=nx.Graph()
        G.add_nodes_from(V)
        G.add_edges_from(edgelist)
        print(len(G))
        nx.draw(G,pos=nx.spring_layout(G),node_size = 10,with_labels = True)
        plt.show()

###################### PATH #############################
p=os.path.realpath(__file__)
ps=p.split('\\')
ps.pop()
PATH='\\'.join(ps)#\LSNIM\package
print(PATH)
##################### data format ################################

def choose_data(str):
        G=[]
        
        ######## (V,E,L) ########
        
        if str=='movie':
                mf=MovieFormat.MF(PATH)
                node_m=mf.load_node()# nID* [nID,name,weight,type,topicID[]]
                edge_m=mf.load_edge()# eID* [eID,nID1,nID2]
                print(len(node_m),'  ',len(edge_m))

                V_m=[]# nID* [nID]
                L_m=[]# nID* [topicID[]]
                for i in node_m:
                        # Adj_m.append([])
                        V_m.append(i[0])
                        L_m.append(i[4])
                
                E_m=edge_m# eID* [eID,nID1,nID2]
                # a=[]
                # for i in edge_m:
                        # Adj_m[i[1]].append
                G=[V_m,E_m,L_m]
                
        elif str=='citation':
                cf=CitationFormat.CF(PATH)
                cf.set_bean()
                node_c=cf.get_bean('node')# nID* [nID,topicID[]]
                edge_c=cf.get_bean('edge')# eID* [eID,nID1,nID2,topicID[]]
                print('node_c:',len(node_c),'  edge_c:',len(edge_c))

                V_c=[]
                E_c=[[i[0],i[1],i[2]] for i in edge_c]
                L_c=[]
                
                for i in node_c:
                        V_c.append(i[0])
                        L_c.append(i[1])
                        
                # for i in edge_c:
                        # E_c
                        
                G=[V_c,E_c,L_c]
        elif str=='author':
                print('not yet ready....')
        elif str=='random':
                ## G=util.random()
                print('wrong input')
        else:
                print('wrong input')
        ######## ADJ #########
        ADJ=Basic.get_ADJ(G,'dir')
        G.append(ADJ)
        
        return G
        
        
##################### set parameter ################################
def lism_set_parameter():
        G=choose_data('citation')
        # print(G[3][4221])
        T=[0]# target label:single label; multiple label
        K=10

        profit=[0,1]
        model=ICM.ICM(RP)
        lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread

        round=10
        greedy=old_greedy.Old_Greedy(round)
        # greedy=old_greedy.Old_Greedy(round)
##################### run ################################
def run_lism():
        for i in [280,600,311,502,513]:
                print('adj of node',i,':',G[2][i])

        S=greedy.run(G,K,T,lim)
        print(S)

        for i in S:
                print('adj of node',i,':',G[2][i])
        
##################### Test ################################


def multiTest():
        #main
        G=choose_data('citation'，)
        # print(G[3][4221])
        T=[0]# target label:single label; multiple label
        K=50

        profit=[0,1]
        model=ICM.ICM(RP)
        lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread
        # log=[]
        TJts=[0,7,1,3,5,6]
        TJk=[[280,600,311,502,513],[734,757,837,759,811],[1252,1989,1261,280],[77,14,73,105],[311,280,197,236,238],[495,383,388,390,415]]
        K=[1,5,10,20,50]
        Round=[1,10,50]
        # log=[]
        # TJts=[0,0]
        # TJk=[[280,600,311,502,513]]
        # K=[1,5]
        # Round=[1,2]
        for t in TJts:
                print('----------------------[ topic-',t,' ]----------------------')
                for k in K:
                        print('---------- [ K-',k,' ]------------')
                        for r in Round:
                                time1=now()
                                print('----[ Round-',r,' ] ----')
                                greedy=old_greedy.Old_Greedy(r)
                                S=greedy.run(G,k,[t],lim)
                                time2=now()
                                print('------------time:',time2-time1)

def ICTest():
        G=choose_data('citation')
        # print(G[3][4221])
        T=[0]# target label:single label; multiple label
        K=10

        profit=[0,1]
        model=ICM.ICM(RP)
        lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread
        round=1000
        greedy=old_greedy.Old_Greedy(round)
        S=greedy.run(G,K,T,lim)
        print(S)
        
        
ICTest()