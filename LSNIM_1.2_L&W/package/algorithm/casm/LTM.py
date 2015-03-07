#coding=utf-8

class LTM:
        
        V=[]
        E=[]
        P=[]
        TIC=[] #probobility
        A=[]#set of active nodes
        NumOfActivated=[]#num of trying to being activated by neighborhood nodes
        ROUND=10000
        
        def __init__(self,V,E,P):
                print('ICM init...')
                self.V=V
                self.E=E
                self.NumOfActivated=[0 for i in range(len(self.V))]
                
        def propacate_from_v(v,V,E,NumOfActivated):
                round=self.ROUND#round is the number of propacate steps
                adj=[]#adjucit nodes
                Ar=[]#activated nodes in each round
                A=[]#activated nodes in total rounds
                adj=get_adj(v)
                
                # try to activate v's neighborhood
                for a in adj: #!!!!!!! Breadth-first !!!!!!!! 
                        boolean='' # can or can't be activated
                        boolean=activate(v,a)
                        if boolean==0:
                                NumOfActivated[a]+=1
                        else if boolean==1:
                                Ar.append(a)
                                V.remove(a)
                        E.remove(v,a)
                A.extend(Ar)      
                round-=1
                #recurssion or return
                if round>0 and len(V)>0 and len(E)>0:
                        # recurssion
                        for aa in Ar:
                                A=propacate_from_v(aa,V,E,NumOfActivated,round)
                else:
                        return  A

        def activate(v,a):
                #compute possibility
                pva=get_edge_influence_probility(v,a)
                bl=util.random.random_pick([0,1],[pva,1-pva])
                return bl
         
        def get_edge_influence_probility(v,a):
                #1.settled--eg:'Golden Ratio'=0.618
                pva=0.05
                #2.learned from post network
                
                #3.calculate from weight:
                
                return pva
        
        def
                
                