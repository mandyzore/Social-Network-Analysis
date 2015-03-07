#coding=utf-8

import string
from time import clock as now




class LIM:
        
        #mainly deal with the 'labeled-profit' calculation
        
        PROFIT=[]
        MODEL='' #ICM or LTM class object

        
        def __init__(self,P,M):
                self.PROFIT=P
                self.MODEL=M
                print('LabledInfluenceMaxi.LIM init...')
        
        def set_profit(self,p):
                self.PROFIT=p
                
        def set_model(self,m):
                self.MODEL=m
                
        def labeled_influence_spread(self,v,G_,T,NumOfActivated):# objective function.
                R_S=0
                A_S=influence_spread(v,G_,NumOfActivated)#activated node set by S
                for i in A_S:
                        R_S+=profit_value(i,T)
                return R_S # a number of profit value
                
        def influence_spread(self,v,G_,NumOfActivated):
                #propagate model choose
                V=G_[0]
                E=G_[1]
                A_S=self.MODEL.propacate_from_v(v,V,E,NumOfActivated)
                return A_S # a node set 
                
        def get_labels(self,v):
                L_v=self.L[v]
                return L_v 
                
        def profit_value(self,v,T):# calculate v's labeled profit
                try:
                        T.index(v)
                        return self.PROFIT[1]
                except:
                        return self.PROFIT[0]
        
