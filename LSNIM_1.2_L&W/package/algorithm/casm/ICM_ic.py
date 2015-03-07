#coding=utf-8
# import queue

import random as rr


class ICM:
        
        Randomy=''
        Pvu=0
        
        def __init__(self,randomy,pvu):
                print('ICM_ic init...')
		
                self.Randomy=randomy
                self.Pvu=pvu
                
        def activate_countNum(self,v,u,NumOfActivated):
                # No
                if NumOfActivated[u]==-1:# u is already activated
                        result=-1
                        return result
                # First time
                elif NumOfActivated[u]==0:# the first time for u try to be activated
                        #compute possibility
                        pva=self.get_edge_influence_probility(v,u,0)
                        result=self.Random.random_pick([0,1],[pva,1-pva])
                        return result
                # Mandy times
                elif NumOfActivated[u]>0:# the nTH time for u try to be activated
                        ##compute possibility with 'NumOfActivated weight'!
                        pva=self.get_edge_influence_probility(v,u,0)
                        result=self.Random.random_pick([0,1],[pva,1-pva])
                        return result
                        
        def activate_simple(self,v,u):
                pva=self.Pvu
                x=rr.uniform(0,1)
		#print('rr.uniform:',x)
                result=self.Randomy.random_pick([0,1],[pva,1-pva],x)
                return result
                
        def get_edge_influence_probility_multi(self,v,u,one):
                #1.settled--eg:'Golden Ratio'=0.618
                if one==0:
                        pva=0.05 
                #2.learned from post network
                elif one==1:
                        pva=TIC[v][u] 
                #3.calculate from weight:
                elif one==2:
                        w=2
                return pva
        
        def get_edge_influence_probility_simple(self,v,u):
                pva=0.01
                return pva
                
        def propacate_from_v_one_step(self,v,G):# ......
                ## only take one propacate steps
                A=[]
                adj=G[3][v]
                NumOfActivated=[0 for i in range(len(ADJ)) ]
                # try to activate v's neighborhood
                count=1
                
                for a in adj: #!!!!!!! Breadth-first !!!!!!!! 
                        # print('# node ',v,'’ ',count,'TH neiborghood..')
                        result=self.activate(v,a,NumOfActivated)
                        if result==0: # un-successed
                                NumOfActivated[a]+=1
                        elif result==1: # successed
                                A.append(a)
                                NumOfActivated[a]=-1
                        count+=1
                return  A
                
        def propacate_from_S(self,S,G):# ......
                ## one time simulation in G
                
                ## activate_simple()
                
                V=G[0]
                ADJ=G[3]
                Queue=[i for i in S]
                Color=[0 for i in range(len(V)) ]# |V| # BFS color [0->1]
                ActiveNode=[i for i in S]
                ActiveEdge=[]
                
                #---BFS---propagate-----------------------------------------------------------
                while True:
                        if len(Queue)==0:
                                break
                                
                        q=Queue.pop(0) # orders do matter or not ???---> !!!!!!  the hesd in Q
                        #--Try-activate-neighborhood------------
                        adj=ADJ[q]
                        activeE=[]
                        activeN=[]
                        
                        for a in adj:
                                if Color[a]==1:# already active
                                        continue
                                else:
                                        result=self.activate_simple(q,a)
                                        if result==1: # successed
                                                Color[a]=1
                                                activeN.append(a)
                                                activeE.append([q,a])
                        Queue.extend(activeN)
                        ActiveNode.extend(activeN)
                        ActiveEdge.extend(activeE)
                        
                return  [ActiveNode,ActiveEdge]
                
        def propacate_from_v_depth(self,v,G):# ......
                ## one time simulation in G
                
                V=G[0]
                ADJ=G[3]
                # Vtmp=[i for i in V]
                Queue=[v]
                Color=[0 for i in range(len(V)) ]# |V| # BFS color [0->1]
                ActiveNode=[v]
                ActiveEdge=[]
                
                P=[[]]
                depth=0
                level1=len(Queue)
                level2=0
                #---BFS---propagate-----------------------------------------------------------
                while True:
                        if len(Queue)==0:
                                break
                                
                        print('depth:',depth)
                        q=Queue.pop(0) # orders do matter or not ???---> !!!!!!  the hesd in Q
                        P[depth].append(q)
                        level1-=1
                        
                        if level1==0:
                                depth+=1# enter a new BFS level
                                P.append([])
                                level1=level2
                                level2=0
                                
                        
                        #--Try-activate-neighborhood------------
                        adj=ADJ[q]
                        activeE=[]
                        activeN=[]
                        for a in adj:
                                if Color[a]==1:# already active
                                        continue
                                else:
                                        result=self.activate_simple(v,a)
                                        if result==1: # successed
                                                Color[a]=1
                                                activeN.append(a)
                                                activeE.append([q,a])
                        Queue.extend(activeN)
                        ActiveNode.extend(activeN)
                        ActiveEdge.extend(activeE)
                        P[depth].append(activeN)
                        
                        level2+=len(activeN)

                        
                        
                return  [[ActiveNode,ActiveEdge],P]
                
        def propacate_from_v_draw(self,v,G):
                ## one time simulation in G
                
                ## activate_simple()
                
                V=G[0]
                ADJ=G[3]
                Queue=[v]
                Color=[0 for i in range(len(V)) ]# |V| # BFS color [0->1]
                ActiveNode=[v]
                ActiveEdge=[]
                
                #---BFS---propagate-----------------------------------------------------------
                while True:
                        if len(Queue)==0:
                                break
                                
                        q=Queue.pop(0) # orders do matter or not ???---> !!!!!!  the hesd in Q
                        #--Try-activate-neighborhood------------
                        adj=ADJ[q]
                        activeE=[]
                        activeN=[]
                        for a in adj:
                                if Color[a]==1:# already active
                                        continue
                                else:
                                        result=self.activate_simple(v,a)
                                        if result==1: # successed
                                                Color[a]=1
                                                activeN.append(a)
                                                activeE.append([q,a])
                        Queue.extend(activeN)
                        ActiveNode.extend(activeN)
                        ActiveEdge.extend(activeE)
                        
                return  [ActiveNode,ActiveEdge]

        def propacate_from_v(self,v,G):
                ## one time simulation in G
                
                ## activate_simple()
                
                V=G[0]
                ADJ=G[3]
                Queue=[v]
                Color=[0 for i in range(len(V)) ]# |V| # BFS color [0->1]
                ActiveNode=[v]
                ActiveEdge=[]
                
                #---BFS---propagate-----------------------------------------------------------
                while True:
                        if len(Queue)==0:
                                break
                                
                        q=Queue.pop(0) # orders do matter or not ???---> !!!!!!  the hesd in Q
                        #--Try-activate-neighborhood------------
                        adj=ADJ[q]
                        activeE=[]
                        activeN=[]
                        
                        for a in adj:
                                if Color[a]==1:# already active
                                        continue
                                else:
                                        result=self.activate_simple(q,a)
                                        if result==1: # successed
                                                Color[a]=1
                                                activeN.append(a)
                                                activeE.append([q,a])
                        Queue.extend(activeN)
                        ActiveNode.extend(activeN)
                        ActiveEdge.extend(activeE)
                        
                return  [ActiveNode,ActiveEdge]
