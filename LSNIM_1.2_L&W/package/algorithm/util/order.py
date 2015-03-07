#coding=utf-8

import string
from time import clock as now


class ICM:
        
        S=[]
        V=[]
        P=[]
        TIC=[] #probobility
        A=[]#set of active nodes
        NumOfActivated=[]#num of trying to being activated by neighborhood nodes
        
        def __init__(self,S,V,P):
                print('ICM init...')
                
        def propacate_from_v(v,V,E,NumOfActivated,round):
                #round is the number of propacate steps
                adj=[]#adjucit nodes
                Ar=[]#activated nodes in each round
                A=[]#activated nodes in total rounds
                adj=get_adj(v)
                
                # try to activate v's neighborhood
                for a in adj: #!!!!!!! Breadth-first !!!!!!!! 
                        boolean='' # can or can't be activated
                        boolean=activate(v,a)
                        if boolean==o:
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
                pva=get_inf_pos(v,a)
                bl=round_01(pva)
                return bl
         
        def get_inf_pos(v,a,one):
                
                
                return pva
                