#coding=utf-8

# import sys
# sys.path.append('..')
# print(sys.path)

from time import clock as now




class Seed_Region:
        
        TJts=[0,7,1,3,5,6]
        TJk=[[280,600,311,502,513],[734,757,837,759,811],[1252,1989,1261,280],[77,14,73,105],[311,280,197,236,238],[495,383,388,390,415]]
        
        
        
        def __init__(self):
                print('Seed_Region init...')
                
        def evaluate_weak_edge(self,e,ADJ,V):
                
                return ture
            
        def split_region(self,G):
                region=[]
                return region
                
                
        def run(self,G,K,T,ICM):
                print('----Seed_Region algorithm start running....')
                
                #引用
                NodeNum=len(G[0])
                V=[i for i in range(NodeNum)]
                
                E=[i for i in G[1]]
                L=[i for i in G[2]]
                ADJ=[i for i in G[3]]
                
                ADJre=[[] for i in range(NodeNum)]# reverse ADJ
                for i in E:
                        nid1=i[1]
                        nid2=i[2]
                        if nid1 not in ADJ[nid2]:
                                ADJ[nid2].append(nid1)
                
                E_mark=['plain' for i in range(len(E))]

                #
                # for i in range(NodeNum):
                        # ADJJ.append([])
                        # for ii in ADJ[i]:
                                # ADJJ[i].append()
                        # if len(ADJ[i])==0:
                                # VV.remove(i)
                                
                S=[]
                Region=[]
                
                # for k in range(K): #??????
                        
                # 1. derive GG: evaluate weak-edge and remove----------------------1
                for e in E:
                        # if self.evaluate_weak_edge(e,ADJ,ADJre,E):
                        
                        v=e[1]
                        u=e[2]
                        tmpt=[]
                        
                        rs=True
                        for ti in T:
                                if (L[v][ti]==0)&(L[u][ti]==0):
                                        for av in ADJre[v]:
                                                if(L[v][ti]>0):
                                                        re=False
                                        for au in ADJ[u]:
                                                if(L[u][ti]>0):
                                                        re=False     
                        if re==True:
                                E_mark[e[0]]='weak'
                                ADJJ[v].remove(u)
                        
                
                
                # 2. split selection region----------------------------------------2
                
                
                
                region=        
                        
                
                # 3. select seed---------------------------------------------------3
              


                for v in range(NodeNum):
                        for u in ADJ[v]:
                                for t in T:
                                        if t in L[u]:
                                                ddv[v]=ddv[v]+1
                                
                
                tv=[0 for i in range(NodeNum)] # v's seed neighbor in T
                rv=[0 for i in range(NodeNum)] # v's seed neighbor not in T
                
                #------------------------valadite-------------------------------
                Topic=T[0]
                TK=self.TJk[self.TJts.index(Topic)]
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
                                        if i in TK:
                                                print('---TJ--',i,':',ddv[i])
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
                                                if t in L[seed]:
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
                                                                if t in L[adju]:
                                                                        pf+=1
                                                        Profitadju+=pf*pvu
                                        Profitu+=Profitadju
                                        # update degree
                                        ddv[u]=P*Profitu
                
                        time3=now()
                        timegap=time3-time2
                        
                return S,ddv

