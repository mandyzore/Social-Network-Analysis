#coding=utf-8

# import sys
# sys.path.append('..')
# print(sys.path)

from time import clock as now




class Degree_Discount:
        
        TJts=[0,7,1,3,5,6]
        TJk=[[280,600,311,502,513],[734,757,837,759,811],[1252,1989,1261,280],[77,14,73,105],[311,280,197,236,238],[495,383,388,390,415]]
        
        def __init__(self):
                print('Degree_Discount init...')
                
        
        def run(self,G,K,T,ICM):
                print('----Degree_Discount algorithm start running....')
                
                #引用
                NodeNum=len(G[0])
                print('NodeNum:',NodeNum)
                
                V=[i for i in range(NodeNum)]
                print('V_ len:',len(V))
                # print(V_[])
                E=[i for i in G[1]]
                L=[i for i in G[2]]
                ADJ=[i for i in G[3]]
                
                S=[]
                dv=[len(a) for a in ADJ] # v's total neighbor
                ddv=[0 for i in range(NodeNum)]
                
                #intialize ddv with topic-based score
                for v in range(NodeNum):
                        for u in ADJ[v]:
                                for t in T:
                                        if L[u][t]>0:
                                                ddv[v]=ddv[v]+1
                                
                
                tv=[0 for i in range(NodeNum)] # v's seed neighbor in T
                rv=[0 for i in range(NodeNum)] # v's seed neighbor not in T
                
                #------------------------valadite-------------------------------
                # Topic=T[0]
                # TK=self.TJk[self.TJts.index(Topic)]
                #---------------------------------------------------------------
                
                
                timegap=0
                #---------------K Seed Run ----------------------------------------------------------------
                for k in range(K):# seeds set num: K
                        print('### start selecting the ',k,'th seed ...')
                        time1=now()
                        
                        # select max seed------------------------
                        max_ddv=-1
                        seed=-1
                        for i in range(NodeNum):
                                if i not in S:
                                        if ddv[i]>max_ddv:
                                                max_ddv=ddv[i]
                                                seed=i
                                        # if i in TK:
                                                # print('---TJ--',i,':',ddv[i])
                        S.append(seed)
                        V.remove(seed)
                        time2=now()
                        print('---A seed is added: ',seed,'.--Total Neighbors is ',len(G[3][seed]),'. --Total profit is ',max_ddv,'\n this seed selection takes ',(time2-time1+timegap),' s')
                        print(S)
                                                
                        
                        # discount seed's neighbor------------------------
                        for u in ADJ[seed]:
                                if u not in S:
                                        tar=False
                                        ProfitSeed=0
                                        for t in T:
                                                if L[seed][t]>0:
                                                        tar=True
                                                        ProfitSeed+=1
                                        if t==True:
                                                tv[u]+=1
                                        else:
                                                rv[u]+=1
                                                
                                        pvu=ICM.Pvu
                                        P=1
                                        for exp in range(tv[u]+rv[u]):
                                                P=P*(1-pvu)
                                        
                                        # potaintial influence of u 
                                        Profitu=1
                                        Profitadju=0
                                        for adju in ADJ[u]:
                                                if adju not in S:
                                                        pf=0
                                                        for t in T:
                                                                if L[adju][t]>0:
                                                                        pf+=1
                                                        Profitadju+=pf*pvu
                                        Profitu+=Profitadju
                                        # update degree
                                        ddv[u]=P*Profitu
                
                        time3=now()
                        timegap=time3-time2
                        
                return S,ddv