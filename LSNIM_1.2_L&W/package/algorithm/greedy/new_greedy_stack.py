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
                                ReachableS.append(u)
                                self.DFS_visit_S(u,ADJ,Colors,ReachableS)
                                
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
                ReachableV=[[] for i in ADJ]# reachable node list for each v in V
                Colors=['white' for i in range(len(ADJ)) ]# white |green| black gray
                for i in S:
                        Colors[i]='green'
                
                #---DFS---propagate---Tree-------------------------------------------
                
                #1.compute RS
                for s in S:
                        
                        self.DFS_visit_S(s,ADJ,Colors,ReachableS)
                        # Reachers[s]=Count
                ReachableS=sorted(ReachableS)
                # print('-------S:',str(S),'---------')
                # print('-------ReachableS:',str(ReachableS),'---------')
                
                
                #2.compute Rv: V\(S+RS)
                for v in V:
                        if v not in ReachableS: #剩余的所有点
                                if Colors[v]=='white':
                                        # print('DFS-v:',v)
                                        self.DFS_visit_v(v,ADJ,Colors,ReachableV)
                        
                return ReachableS,ReachableV,Colors
                
        def reach2(self,S,V,ADJ):
                ADJJ=[]
                for i in range(len(ADJ)):
                        ADJJ.append([])
                        for ii in ADJ[i]:
                                ADJJ[i].append(ii)
                # ADJm=[[] for i in range(len(ADJ))]
                EN=0
                
                ReachableS=[]
                ReachableV=[[] for i in ADJ]# reachable node list for each v in V
                Colors=['white' for i in range(len(ADJ)) ]# white |green| black gray
                for i in S:
                        Colors[i]='green'
                
                #---DFS---propagate---Tree-------------------------------------------
                
                # 1.compute RS
                stackS=[s for s in S]
                adjM=[[ item_a for item_a in ADJ[s]] for s in S]
                while 1:
                        if len(stackS)==0:
                                break
                                
                        item=stackS[len(stackS)-1] # 最新添点 index 最右
                        index=len(stackS)-1
                        Colors[item]='gray'
                        
                        for a in adjM[index]:
                                if Colors[a]=='white':
                                        stackS.append(a)
                                        adjM.append([ a_a for a_a in ADJ[a]])
                                        ReachableS.append(a)
                                        Colors[a]='gray'
                                        EN+=1
                                        adjM[index].remove(a)
                                        break
                                elif Colors[a]=='green':
                                        adjM[index].remove(a)
                                elif Colors[a]=='gray':
                                        adjM[index].remove(a)
                                        print('-------------------gray-gray-----G contain CIRCLE !!!!')
                                        
                        if len(adjM[len(stackS)-1])==0:
                                one=stackS.pop()
                                if one!=item:
                                        print('------------------- Wrong -------------------')
                                Colors[item]='green'
                ReachableS=sorted(ReachableS)
                
                # 2.compute Rv: V\(S+RS)
                stackv=[]
                adjM=[]
                for v in V:
                        if v not in ReachableS: #剩余的所有点
                                if Colors[v]=='white':
                                        stackv=[v] # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!directed graph- the different!!
                                        
                                        adjM.append([ v_a for v_a in ADJ[v]])
                                        while 1:# 对stackv中的元素
                                                if len(stackv)==0:
                                                        break
                                                item=stackv[len(stackv)-1] # 最新添点
                                                Colors[item]='gray'
                                                index=len(stackv)-1
                                                # adjM.append([ item_a for item_a in ADJ[item]])
                                                adj_item=adjM[index]
                                                
                                                for a in adjm:
                                                        if Colors[a]=='white':
                                                                stackv.append(a)
                                                                adjM.append([ a_a for a_a in ADJ[a]])
                                                                ReachableS.append(a)
                                                                Colors[a]='gray'
                                                                EN+=1
                                                                adjM[index].remove(a)
                                                                break
                                                        elif Colors[a]=='black':
                                                                adjM[index].remove(a)
                                                                for ar in ReachableV[a]:
                                                                        if ar not in ReachableV[item]:
                                                                                ReachableV[item].append(ar)
                                                        elif Colors[a]=='gray':
                                                                adjM[index].remove(a)
                                                                print('-------------------gray-gray-----G contain CIRCLE !!!!')
                                                                
                                                if len(adjM[len(stackv)-1])==0:
                                                        one=stackv.pop()
                                                        adjM.pop()
                                                        if one!=item:
                                                                print('------------------- Wrong -------------------')
                                                                print('stackv:',stackv,'\n adjM:',adjM)
                                                        Colors[item]='black'
                                                
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ total dfs EN:',EN)
                return ReachableS,ReachableV,Colors

                        
        def run(self,G,K,T,ICM):
                print('----new_greedy algorithm start running....')
                S=[]# seeds set
                # sv=[0 for i in range(len(G[0]))]
                V=[i for i in range(len(G[0]))]# candidated seeds set
                
                E=[i for i in G[1]]
                L=[i for i in G[2]]
                
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
                        sv=[0 for i in range(len(G[0]))]
                        
                        # ROUND times simulations
                        for r in range(self.ROUND):
                                # print('##start ',r,' round ...')
                                time11=now()
                                # 1.compute p for E--------------------------
                                PE=[]
                                for j in E: #5679 [eID,nID1,nID2]
                                        result=ICM.activate_simple(j[1],j[2])
                                        PE.append(result)
                                        
                                # 2.remove e，G1--------------------------
                                ADJ=[]
                                for j in range(len(G[0])):# Node
                                        ADJ.append([])
                                        for jj in G[3][j]: # Adj
                                                ADJ[j].append(int(jj))
                                                
                                for j in range(len(PE)):
                                        if PE[j]==0:
                                                # print('Remove e:',E[j])
                                                ADJ[E[j][1]].remove(E[j][2]) # E:[eID,nID1,nID2]
                                                # c+=1
                                                
                                # 3.DFS & compute RS--------------------------
                                [ReachableS,Reachers,Colors]=self.reach2(S,V,ADJ)
                                
                                
                                for j in range(len(G[0])):# all node
                                        
                                        if Colors[j]!='green': # j not in RS
                                                # label-based
                                                for reacher in Reachers[j]:
                                                        for jj in T:# calculate each topic score
                                                                if L[reacher][jj]>0:# node contain Target topic,score!!
                                                                        sv[j]+=1
                                                                else:
                                                                        sv[j]+=0 # potation to insterested in the Target topic
                                        else:
                                                sv[j]+=0 # !!got 0 score in this Round 
                                        
                                time22=now()
                                # print('^^^^^this round takes :',time22-time11,' s .. ^^^^^')

                        # average simulation & MAX_SV
                        for i in range(len(V)):
                                if V[i] not in S:
                                        v=V[i]
                                        sv[v]=sv[v]/self.ROUND
                                        
                                        if max_sv<sv[v]:
                                                max_sv=sv[v]
                                                max_v=V[i]
                                                
                                        # if v in TK:
                                                # print('---TJ--',v,':',sv[v],' ADJ=',len(G[3][v]),'---')
                                        
                        # add seed
                        S.append(max_v)
                        print('max_v:',max_v)
                        V.remove(max_v)
                        time2=now()
                        
                        print('%%% A seed is added: ',max_v,'. %%% Total Neighbors is ',len(G[3][max_v]),'. %%% Total profit is ',max_sv,'\n this seed selection takes ',time2-time1,' s')
                        
                return S
