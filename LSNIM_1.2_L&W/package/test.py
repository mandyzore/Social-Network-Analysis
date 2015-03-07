import sys
import os
import string
from time import clock as now__all__ 
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
        
        def choose_data(self,str,er,PATH):
                G=[]
                
                ######## (V,E,L) ########
                
                if str=='movie':
                        mf=MovieFormat.MF(self.PATH)
                        
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
                        cf=CitationFormat.CF(self.PATH)
                        print(self.PATH)
                        # cf.set_bean()
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
                ADJ=Basic.get_ADJ(G,er)
                G.append(ADJ)
                
                return G
                
                
        ##################### set parameter ################################

        def RandomTest():
                count0=0
                count1=0
                pva=0.3
                for i in range(100):
                        n=RP.random_pick([0,1],[pva,1-pva])
                        if n==0:
                                count0+=1
                        else:
                                count1+=1
                        print(n)
                        
                print('0:',count0,'  1:',count1)
                
        def ICMTest(v):
                G=choose_data('citation','dir')
                icm=ICM_ic.ICM(RP,0.01)
                pTree=icm.propacate_from_v_draw(v,G)
                print('A_V:',len(pTree[0]),)
                
                G=nx.Graph()
                G.add_nodes_from(pTree[0])
                G.add_edges_from(pTree[1])
                pos=nx.spring_layout(G)
                colors=range(len(pTree[1]))
                # colors=[i for i in range(len(pTree[1]))]
                # colors.reverse()
                nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=True)
                # plt.savefig("edge_colormap.png") # save as png
                plt.show()

                
        def K1Test():
                G=choose_data('citation','dir')
                T=[1]# target label:single label; multiple label
                K=10
                profit=[0,1]
                model=ICM_ic.ICM(RP,0.01)
                lim=LabledInfluenceMaxi.LIM(profit,model)  #labeled_influence_spread
                round=1
                
                greedy=old_greedy_ic.Old_Greedy(round)
                S=greedy.run(G,K,T,lim)
                print(S)
                
                return S

                
        # ICMTest(280)
        # S=K1Test()

        # for i in S:
                # ICMTest(i)

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
                
        def main(self):
                
                data=''
                dir=''
                k=-1
                r=-1
                alg=''
                if platform.python_version()[0]=='2':
                        while 1:
                                data = raw_input("data=")
                                if data not in ['citation','movie']:
                                        print('Wrong input: please input movie or citation!')
                                        continue
                                else:
                                        break
                        while 1:
                                dir = raw_input("graph (dir or undir) = ")
                                if dir not in ['dir','undir']:
                                        print('Wrong input: please choose dir or undir!')
                                        continue
                                else:
                                        break
                                        
                        while 1:
                                k = int(raw_input("Num of Seed K= "))
                                if k <=0 :
                                        print('Wrong input: please input a number (K > 0)!')
                                        continue
                                else:
                                        break
                        while 1:
                                r = int(raw_input("Num of Simulation Round= "))
                                if r <=0 :
                                        print('Wrong input: please input a number (Round > 0)!')
                                        continue
                                else:
                                        break
                                        
                        if alg in['ng','og']:
                                while 1:
                                        r = int(input("Num of Simulation Round= "))
                                        if r <=0 :
                                                print('Wrong input: please input a number (Round > 0)!')
                                                continue
                                        else:
                                                break
                                
                elif platform.python_version()[0]=='3':
                                                      
                        while 1:
                                data = input("data=")
                                if data not in ['citation','movie']:
                                        print('Wrong input: please input movie or citation!')
                                        continue
                                else:
                                        break
                        while 1:
                                dir = input("(dir or undir) graph= ")
                                if dir not in ['dir','undir']:
                                        print('Wrong input: please choose dir or undir!')
                                        continue
                                else:
                                        break
                        while 1:
                                alg = input("lism algorithm= ")
                                if alg not in ['og','ng','dd']:
                                        print('Wrong input: please choose ng or og !')
                                        continue
                                else:
                                        break  
                        
                        while 1:
                                k = int(input("Num of Seed K= "))
                                if k <=0 :
                                        print('Wrong input: please input a number (K > 0)!')
                                        continue
                                else:
                                        break
                                        
                        if alg in['ng','og']:
                                while 1:
                                        r = int(input("Num of Simulation Round= "))
                                        if r <=0 :
                                                print('Wrong input: please input a number (Round > 0)!')
                                                continue
                                        else:
                                                break
                        
                
                
                print('\n-----------------------------------------------------')
                print('Data:',data,'; graph:',dir,'; K=',k,'; Round=',r,'; algorithm:',alg,';')
                print('-----------------------------------------------------\n')
                [G,S,sv]=self.t(data,dir,k,r,alg)
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

# print(sys.argv)
# commd=[sys.argv[i] for i in range(1, len(sys.argv))]

# print(commd)
# test.t(commd[0],commd[1],int(commd[2]),int(commd[3]),commd[4])

# V=[i for range(11)]
# E=[[0,1,2],[1,1,3],[2,1,4],[3,3,5],[4,4,5],[5,6,8],[6,6,7],[7,6,10],[8,7,8],[9,7,9]]
# L=[[0],[0],[0],[0],[0],[0],[0],[0],[0],]


# test=Test()
# S=[]
# G=[]
# sv=[]
# [G,S,sv]=test.main()

def anaylise(K,T,fp):
        
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        Gc=test.choose_data('citation','dir',test.PATH)
        GG=[Gc]
        # K=[i for i in range(50)]# 1-50
        # T=[4]# target label:single label; multiple label
        model=ICM_ic.ICM(RP,0.01)
        profit=[0,1]
        lim=LabledInfluenceMaxi.LIM(profit,model)
        round1=5
        round2=5
        # og=old_greedy.Old_Greedy()

        # og=old_greedy_ic.Old_Greedy(round1)
        # ng=new_greedy.New_Greedy(round2)
        # dd=degree_discount.Degree_Discount()
        # sr=s_r.S_R()
        
        S=[]
        Time=[]
        I=[]
        RanS=[]
        
        import random
        for ig in range(len(GG)):
                S.append([])
                Time.append([])
                I.append([])
                RanS.append([])
                for ik in range(len(K)):
                        S[ig].append(['' for j in range(5)])
                        RanS[ig].append([])
                        for ii in range(K[ik]):
                                x=random.randint(0, (len(GG[ig][0])-1))
                                RanS[ig][ik].append(x)
                        
                        I[ig].append([0 for j in range(5)])
                        Time[ig].append([0 for j in range(4)])
        
        print(RanS)
        print(len(RanS))
        alg=['og','ng','dd','sr']
        for gi in range(len(GG)) :
                G=GG[gi]
                print('========================= G:',gi,' =========================')
                for ki in range(len(K)):
                        # og=old_greedy_ic.Old_Greedy(round1)
                        # ng=new_greedy_stack2.New_Greedy(round2)
                        dd=degree_discount.Degree_Discount()
                        sr=s_r.S_R()
                        print('========================= K:',K[ki],' =========================')
                        print('========================= S =========================')
                        #-------------------------------------------og---
                        time1=now()
                        S[gi][ki][0]=[]#og.run(G,K[ki],T,lim)
                        time2=now()
                        Time[gi][ki][0]=time2-time1
                        #-------------------------------------------ng---
                        time1=now()
                        S[gi][ki][1]=[]#ng.run(G,K[ki],T,model)
                        time2=now()
                        Time[gi][ki][1]=time2-time1
                        #-------------------------------------------dd---
                        time1=now()
                        [S[gi][ki][2],ddvdd]=dd.run(G,K[ki],T,model)
                        time2=now()
                        Time[gi][ki][2]=time2-time1
                        #-------------------------------------------sr---
                        time1=now()
                        [S[gi][ki][3],ddvsr]=sr.run(G,K[ki],T,model)
                        time2=now()
                        Time[gi][ki][3]=time2-time1
                        #------------------------------------------------
                        S[gi][ki][4]=RanS[gi][ki]
                        #------------------------------------------------
                        print('================= Influence Spread ==================')
                        for j in range(5):
                                I[gi][ki][j]=lim.labeled_influence_spread_S(S[gi][ki][j],G,T)
                                
        
        fi=open(test.PATH+'\\'+fp,'w')
        fi.write(str(S)+'\n\n')
        fi.write(str(I)+'\n\n')
        fi.write(str(Time)+'\n\n')
        fi.close()
        return [S,I,Time]
# test.testDraw()
# T=[4,5,6,7,8,9]
# K=[i for i in range(51)]# 1-50
# for t in T:
        # fp='Mt'+str(t)+'k'+str(len(K)-1)+'ngddsr.dat'
        # [S,I,Time]=anaylise(K,[int(t)],fp)

# anaylise([50],[0],'result.dat')

def graphAttribute():
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        Gc=test.choose_data('citation','dir',test.PATH)
        import networkx as nx
        import matplotlib.pyplot as plt
        
        [V,E,L,A]=Gc
        edge=[(i[1],i[2]) for i in E]
        G=nx.DiGraph()
        G.add_nodes_from(V)
        G.add_edges_from(edge)
        vn=len(V)
        en=len(edge)
        maxd=0
        averd=0
        for i in range(vn):
                averd+=G.degree(i)
                if G.degree(i)>maxd:
                        maxd=G.degree(i)
        averd=averd/vn
        
        # print(nx.degree_histogram(G))
        # print(len(nx.degree_histogram(G)))
        # print(len(nx.average_clustering(G)))
        # print(nx.diameter(G))
        # print(len(nx.connected_component_subgraphs(G)))
        print('--',maxd)
        print('--',averd)
        
        
# graphAttribute()
        

def testNG():
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        Gc=test.choose_data('citation','dir',test.PATH)

        K=10
        round=1
        T=[0]# target label:single label; multiple label
        model=ICM_ic.ICM(RP,0.01)
        ng=new_greedy_stack2.New_Greedy(round)

        S=ng.run(Gm,K,T,model)
        print(S)
        
def testOG():
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        # Gc=test.choose_data('citation','dir',test.PATH)
        # GG=[Gc,Gm]
        # K=[i+1 for i in range(2)]# 1-50
        T=[0]# target label:single label; multiple label
        model=ICM_ic.ICM(RP,0.01)
        # profit=[0,1]
        # lim=LabledInfluenceMaxi.LIM(profit,model)
        round1=1
        # round2=5
        og=old_greedy_ic.Old_Greedy(round)
        # ng=_greedy.New_Greedy(1)
        # sr=s_r.S_R()

        og.run(Gm,10,T,model)
def testDD():
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        # Gc=test.choose_data('citation','dir',test.PATH)
        # GG=[Gc,Gm]
        # K=[i+1 for i in range(2)]# 1-50
        T=[0]# target label:single label; multiple label
        model=ICM_ic.ICM(RP,0.01)
        # profit=[0,1]
        # lim=LabledInfluenceMaxi.LIM(profit,model)
        # round1=5
        # round2=5
        # og=old_greedy_ic.Old_Greedy(round1)
        ng=new_greedy.New_Greedy(1)
        # sr=s_r.S_R()

        ng.run(Gm,10,T,model)
def testSR():
        test=Test()
        Gm=test.choose_data('movie','dir',test.PATH)
        # Gc=test.choose_data('citation','dir',test.PATH)
        T=[0]# target label:single label; multiple label
        model=ICM_ic.ICM(RP,0.01)
        sr=s_r.S_R()
        sr.run(Gm,10,T,model)
        
# testNG()
# testSR()
        
# testOG()


k=50
n=3000

N=1
M=1

for i in range(50):
        t=n-i
        M=M*t
        N=N*(i+1)
        
print 


