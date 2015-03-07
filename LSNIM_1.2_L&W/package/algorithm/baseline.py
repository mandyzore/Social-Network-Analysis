#coding=utf-8

# import sys
# sys.path.append('..')
# print(sys.path)

from time import clock as now




class New_Greedy:
        
        ROUND=0
        TJts=[0,7,1,3,5,6]
        TJk=[[280,600,311,502,513],[734,757,837,759,811],[1252,1989,1261,280],[77,14,73,105],[311,280,197,236,238],[495,383,388,390,415]]
        
        def __init__(self,round):
                self.ROUND=round
                print('new_greedy init...')
                
                
        def DFS_visit_S(self,v,ADJ,Colors,ReachableS):
                Colors[v]='gray'
                # print('DFS_visit:',v)
                # print(v,' neighbor:',ADJ[v])
                for u in ADJ[v]:
                        if Colors[u]=='white':
                                
                                self.DFS_visit_S(u,ADJ,Colors,ReachableS)
                                ReachableS.append(u)
                                
                Colors[v]='green'
                return 
        
        def DFS_visit_v(self,v,ADJ,Colors,ReachableV):
                Colors[v]='gray'
                # print('DFS_visit_v:',v)
                # print(v,' neighbor:',ADJ[v])
                
                for u in ADJ[v]:
                        ReachableV[v].append(u)
                        
                        if Colors[u]=='white':
                                # print('DFS_visit_v:',u)
                                self.DFS_visit_v(u,ADJ,Colors,ReachableV)
                        elif Colors[u]=='black':
                                # 1. append
                                for n in ReachableV[u]:
                                        if n not in ReachableV[v]:
                                                ReachableV[v].append(n)
                                # 2. extend      
                                # ReachableV[v].extend(ReachableV[u])
                                
                Colors[v]='black'
                # ReachableV[]
                return
                
        def reach(self,S,V,ADJ):
                 
                ReachableS=[]
                # ReachNum=[-1 for i in ADJ]
                ReachableV=[[] for i in ADJ]# reachable node list for each v in V
                Colors=['white' for i in range(len(ADJ)) ]# white |green| black gray
                for i in S:
                        Colors[i]='green'
                
                # V=[i for i in range(len(ADJ))]
                #---DFS---propagate---Tree-------------------------------------------
                
                #compute RS
                for s in S:
                        # if Colors[s]==0:
                        # print('DFS-s:',s)
                        self.DFS_visit_S(s,ADJ,Colors,ReachableS)
                        # Reachers[s]=Count
                
                
                #compute Rv: V\(S+RS)
                for v in V:
                        if v not in ReachableS: #剩余的所有点
                                if Colors[v]=='white':
                                        # print('DFS-v:',v)
                                        self.DFS_visit_v(v,ADJ,Colors,ReachableV)
                        
                return ReachableS,ReachableV,Colors
                

                        
        def run(self,G,K,T,ICM):
                print('----greedy algorithm start running....')
                S=[]# seeds set
                V=[i for i in G[0]]# candidated seeds set
                E=[i for i in G[1]]
                L=[i for i in G[2]]
                print('L:',L[0])
                print('T',T)
                # ADJ=[i for i in G[3]]
                #------------------------valadite-------------------------------
                Topic=T[0]
                TK=self.TJk[self.TJts.index(Topic)]
                #---------------------------------------------------------------
                
                #---------------K Seed Run --------------------------------------
                for k in range(K):# seeds set num: K
                        print('### start selecting the ',k,'th seed ...')
                        
                        time1=now()
                        max_sv=0
                        max_v=-1
                        sv=[0 for i in G[0]]
                        print('sv len:',len(sv))
                        
                        # ROUND times simulations
                        for r in range(self.ROUND):
                                print('##start ',r,' round ...')
                                
                                # 1.compute p for E--------------------------
                                PE=[]
                                for j in E:# 5790
                                        result=ICM.activate_simple(j[1],j[2])
                                        PE.append(result)
                                        
                                # 2.remove e，G1--------------------------
                                ADJ=[]
                                for j in range(len(G[3])):
                                        ADJ.append([])
                                        for jj in G[3][j]:
                                                ADJ[j].append(jj)
                                for j in range(len(PE)):
                                        if PE[j]==0:
                                                # print('Remove e:',E[j])
                                                ADJ[E[j][1]].remove(E[j][2]) # E:[eID,nID1,nID2]
                                                # c+=1
                                # 3.DFS & compute RS--------------------------
                                [ReachableS,Reachers,Colors]=self.reach(S,V,ADJ)
                                for j in V:# candidate
                                        if j not in ReachableS:
                                                # label-based
                                                for reacher in Reachers[j]:
                                                        for jj in T:# for each topic
                                                                if L[reacher][jj]>0:# node contain Target topic,score!!
                                                                        sv[j]+=1
                                                                else:
                                                                        sv[j]+=0.01 # potation to insterested in the Target topic
                                        else:
                                                sv[j]+=0 # !!got 0 score in this Round 
                                        
                                        if j in TK:
                                                print('---TJ--',j,':',sv[j],' Color=',Colors[j],' ADJ=',len(G[3][j]),'---')
                                        
                                # fo=open('test-reach'+str(r)+'.dat','w')
                                # for rj in range(len(Reachers)):
                                        # fo.write(Colors[rj]+str(sv[rj])+' '+str(len(Reachers[rj]))+' '+str(Reachers[rj])+'\n')
                                # fo.close()
                                
                        # average simulation & MAX_SV
                        for vi in V:
                                if vi not in S:
                                        sv[vi]=sv[vi]/self.ROUND
                                        
                                        if max_sv<sv[vi]:
                                                max_sv=sv[vi]
                                                max_v=V[vi]
                                        
                                        
                        
                        # add seed
                        S.append(max_v)
                        print('max_v:',max_v)
                        V.remove(max_v)
                        time2=now()
                        
                        print('%%% A seed is added: ',max_v,'. %%% Total Neighbors is ',len(G[3][max_v]),'. %%% Total profit is ',max_sv,'\n this seed selection takes ',time2-time1,' s')
                        
                return S


        
                
                
                
