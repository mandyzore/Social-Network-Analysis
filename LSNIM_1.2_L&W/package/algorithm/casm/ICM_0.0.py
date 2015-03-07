#coding=utf-8

class ICM:
        
        ROUND=0
        Random=''
        
        def __init__(self,R,r):
                print('ICM init...')
                self.ROUND=R
                self.Random=r
                
        

        def activate(self,v,u):
                #compute possibility
                pva=self.get_edge_influence_probility(v,u,0)
                bl=self.Random.random_pick([0,1],[pva,1-pva])
                return bl
         
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
                
        def propacate_from_v(self,v,ADJ,A,NumOfActivated):
                
                #round is the number of propacate steps
                adj=ADJ[v]
                Ar=[]#activated nodes in each round
                
                # try to activate v's neighborhood
                for a in adj: #!!!!!!! Breadth-first !!!!!!!! 
                        boolean='' # can or can't be activated
                        boolean=self.activate(v,a)
                        if boolean==0:
                                NumOfActivated[a]+=1
                        elif boolean==1:
                                Ar.append(a)
                                A.append(a)
                                # ADJ[]
                        # try:
                                # E.remove([v,a])
                        # except ValueError:
                                # try:
                                        # E.remove([a,v])
                                # except ValueError:
                                        # print('E had removed',[a,v])
                # A.extend(Ar)
                self.ROUND-=1
                #recurssion or return
                if self.ROUND>0 : ## and len(V)>0 and len(E)>0
                        # recurssion
                        for aa in Ar:
                                self.propacate_from_v(aa,ADJ,A,NumOfActivated)
                else:
                        return  A