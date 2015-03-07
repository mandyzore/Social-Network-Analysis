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
                
        def labeled_influence_spread_v(self,v,G,T):# objective function.
                R_S=0
                A=[]
                [A,E]=self.MODEL.propacate_from_v(v,G)#activated node set by S
                L=G[2]
                # print('A len:', len(A))
                for v in A:
                        R_S+=self.profit_value(v,L,T)
                return R_S # a number of profit value
                
        def labeled_influence_spread_S(self,SS,G,T):# objective function.
                R_S=0
                A=[]
                [A,E]=self.MODEL.propacate_from_S(SS,G)#activated node set by S
                L=G[2]
                for v in A:
                        R_S+=self.profit_value(v,L,T)
                return R_S # a number of profit value
                
        def get_labels(self,v):
                L_v=self.L[v]
                return L_v 
                
        def profit_value(self,v,L,T):# calculate v's labeled profit
                for i in T:
                        if L[v][i]!=0:
                                return self.PROFIT[1]
                        else:
                                return self.PROFIT[0]