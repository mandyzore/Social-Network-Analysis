#coding=utf-8
# import queue

class ICM:
        
        Random=''
        
        def __init__(self,r):
                print('ICM init...')
                self.Random=r
        
        def activate(self,v,u,NumOfActivated):
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
                        
        def activate_(self,v,u):
                pva=self.get_edge_influence_probility(v,u,0)
                result=self.Random.random_pick([0,1],[pva,1-pva])
                return result
                
        def get_edge_influence_probility_(self,v,u,one):
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
        
        def get_edge_influence_probility(self,v,u,one):
                pva=0.05 
                return pva
                
        def propacate_from_v(self,v,ADJ):
                ## only take one propacate steps
                A=[]
                adj=ADJ[v]
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
                
        def propacate_from_v_(self,S,ADJ):
                ## one time simulation in G
                A=[]
                # A=[i for i in S]#????????
                Q=[i for i in S]
                Mark=[0 for i in range(len(ADJ)) ]# |V| # BFS color [0->1]
                for i in S:
                        Mark[i]=1 # seed is activated inially
                        
                #BFS--------------------------------------------------------------------
                while True:
                        if len(Q)==0:
                                # print('!!!!!!!!! Q is empty !!!!!!!!!!')
                                break
                        
                        v=Q.pop(0) # orders do matter or not ???---> !!!!!!  the hesd in Q
                        adj=ADJ[v]
                        for a in adj:
                                if Mark[a]==1:
                                        continue
                                else:
                                        result=self.activate_(v,a)
                                        if result==1: # successed
                                                Mark[a]=1
                                                Q.append(a)
                                                A.append(a)
                return  A
                
                
        def propacate_from_v__(self,SS,ADJ):
                ## one time simulation in G
                A=[]
                Q=[]
                Mark=[0 for i in range(len(ADJ)) ]# |V| # BFS color [0->1]
                for i in SS:
                        Mark[i]=1 # seed is activated inially
                        
                #BFS--------------------------------------------------------------------
                Q=SS
                A=SS
                while True:
                        if len(Q)==0:
                                break
                        else:
                                v=Q.pop() # orders do matter or not ???
                                adj=ADJ[v]
                                
                                for a in adj:
                                        if Mark[a]==1:
                                                continue
                                        else:
                                                result=self.activate_(v,a)
                                                if result==1: # successed
                                                        Mark[a]=1
                                                        Q.append(a)
                                                        A.append(a)
                return  A