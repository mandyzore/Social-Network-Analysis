import sys
import os
import string
from time import clock as now
import platform

import networkx as nx
import matplotlib.pyplot as plt

from graph import Basic
from format import MovieFormat
from format import CitationFormat
from algorithm.util import randomy as RP

# from algorithm.greedy import old_greedy
from algorithm.greedy import old_greedy_ic
from algorithm.greedy import new_greedy
from algorithm.greedy import new_greedy_stack2
from algorithm.heuristics import degree_discount
from algorithm.heuristics import s_r
from algorithm.lism import LabledInfluenceMaxi
from algorithm.casm import ICM
from algorithm.casm import ICM_ic




class Test:
        
        PATH=''
        
        def __init__(self):
                p=os.path.realpath(__file__)
                # print(p)
                sysp=''
                if platform.system()=='Windows':
                        sysp='\\'
                elif platform.system()=='Linux':
                        sysp='/'
                ps=p.split(sysp)
                # print(ps)
                ps.pop()
                self.PATH=sysp.join(ps)#\LSNIM\package
                print('-------PATH:',self.PATH)
        
        
        ##################### set parameter ################################

        
        

        def t(self,data,direction,K,round,g):
                S=[]
                G=[]
                sv=[]
                if g=='og':
                        G=self.choose_data(data,direction,self.PATH)
                        T=[0]# target label:single label; multiple label
                        profit=[0,1]
                        model=ICM_ic.ICM(RP,0.01)
                        lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread
                        greedy=old_greedy_ic.Old_Greedy(round)
                        S=greedy.run(G,K,T,lim)
                elif g=='ng':
                        G=self.choose_data(data,direction,self.PATH)
                        T=[0]# target label:single label; multiple label
                        profit=[0,1]
                        model=ICM_ic.ICM(RP,0.01)
                        greedy=new_greedy.New_Greedy(round)
                        S=greedy.run(G,K,T,model)
                elif g=='dd':
                        G=self.choose_data(data,direction,self.PATH)
                        T=[0]# target label:single label; multiple label
                        profit=[0,1]
                        model=ICM_ic.ICM(RP,0.01)
                        heuri=degree_discount.Degree_Discount()
                        [S,sv]=heuri.run(G,K,T,model)
                        
                print(S)
                return [G,S,sv]
                

        def testDraw(self):
                import networkx as nx
                import matplotlib.pyplot as plt

                cf=CitationFormat.CF(self.PATH)
                node_c=cf.get_bean('node')# nID* [nID,topicID[]]
                edge_c=cf.get_bean('edge')# eID* [eID,nID1,nID2,topicID[]]
                nodeNum=len(node_c)
                edgeNum=len(edge_c)
                
                colorn=[]
                colore=[]
                for i in range(nodeNum):
                        mainColor=-1
                        t=node_c[i][1]
                        for ti in range(10):
                                if t[ti]>mainColor:
                                        mainColor=ti        
                        colorn.append(mainColor)
                        
                for i in range(edgeNum):
                        mainColor=-1
                        t=edge_c[i][3]
                        for ti in range(10):
                                one=0
                                if t[ti]==1:
                                        mainColor=ti
                                        one+=1
                        if one>1:
                                colore.append(20)
                        else:
                                colore.append(mainColor)
                                
                V=[]
                Vv=[i for i in range(nodeNum)]
                VV= zip(Vv,colorn)
                print('Vv:',len(Vv))
                
                VV=sorted(VV,key= lambda x:int(x[1]))
                V=[i[0] for i in VV]
                
                edgelist=[(i[1],i[2]) for i in edge_c]#[eID,nID1,nID2,topicID[]]
                
                
                G=nx.Graph()
                G.add_nodes_from(V)
                G.add_edges_from(edgelist)
                print(len(G))
                print('color: ',len(colorn),' ',len(colore))
                print('G:',len(V),' ',len(edgelist))
                bb = nx.betweenness_centrality(G)
                nx.set_node_attributes(G, 'betweenness', bb)
                nx.draw(G,node_color=colorn,pos=nx.spring_layout(G),node_size = 50,with_labels = False) #edge_color=colore,
                plt.savefig("color_c.png") 
                plt.show()
                
##################### data format ################################

