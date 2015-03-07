#coding=utf-8

class ICM:
        
        Random=''
        
        def __init__(self,r):
                print('ICM init...')
                self.Random=r
                
        
        def activate(self,v,u,NumOfActivated):
                
                if NumOfActivated[u]==1:# u is already activated
                        result=-1
                        return result
                        
                elif NumOfActivated[u]==0:# the first time for u try to be activated
                        #compute possibility
                        pva=self.get_edge_influence_probility(v,u,0)
                        result=self.Random.random_pick([0,1],[pva,1-pva])
                        return result
                        
                elif NumOfActivated[u]>1:# the nTH time for u try to be activated
                        ##compute possibility with 'NumOfActivated weight'!
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
                                NumOfActivated[a]+=1
                        count+=1
                return  A