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

def testDraw():
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
        
##################### main ################################


def multiTest():
        #main
        G=choose_data('citation')
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
        Round=[1,5,10,50,100,200,500]

        # log=[]
        # TJts=[0,0]
        # TJk=[[280,600,311,502,513]]
        # K=[1,5]
        # Round=[1,2]
        for t in TJts:
                 # log.append('')
                         # log.append(['----------------------[ Round-',r,' ] 
                 # log.append('')
                 # log.append(['---------------------- [ K-',k,' ]------------------------------------------------------------------'])
                print('----------------------[ topic-',t,' ]----------------------')
                for k in K:
                         # log.append('')--------------------------------------------'])
                        print('---------- [ K-',k,' ]------------')
                        for r in Round:
                                # log.append('')
                                # log.append(['---------------------- [ topic-',t,' ] -------------------'])
                                time1=now()
                                print('----[ Round-',r,' ] ----')
                                greedy=old_greedy.Old_Greedy(r)
                                S=greedy.run(G,k,[t],lim)
                                # log.append('S:['+','.join([str(s) for s in S])+']')
                                time2=now()
                                print('------------time:',time2-time1)
        # f_out=open(PATH+'\\test_citation.txt','w')
        # for s in log:
                # ss=' '
                # for j in s:
                        # ss+=str(j)
                # f_out.write(ss+'\n')
        # f_out.close()
        
        ##import logging
        ## 
        ####logging.basicConfig(filename = 'log.txt', filemode='w', level=logging.DEBUG, format = '%(process)d %(message)s')
        ####logging.debug('debug message')
        ##        	
        ##LOG = logging.getLogger('Fk')
        ##File = logging.FileHandle('log.txt')
        ##format = logging.Formatter('%(process)d %(message)s')
        ##File.setFormatter(format)
        ##LOG.addHandler(File)
        ##LOG.setLevel(logging.DEBUG)
        ##LOG.debug('debug message')
        
def ICTest():
        G=choose_data('citation')
        # print(G[3][4221])
        T=[0]# target label:single label; multiple label
        K=50

        profit=[0,1]
        model=ICM.ICM(RP)
        lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread

