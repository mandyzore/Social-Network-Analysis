#coding=utf-8

# import sys
# sys.path.append('..')
# print(sys.path)

from time import clock as now




class Old_Greedy:
        
        ROUND=0
        TJts=[0,7,1,3,5,6]
        TJk=[[280,600,311,502,513],[734,757,837,759,811],[1252,1989,1261,280],[77,14,73,105],[311,280,197,236,238],[495,383,388,390,415]]
        
        
        
        
        def __init__(self,round):
                self.ROUND=round
                print('old_greedy init...')
        
        
        def run(self,G,K,T,lis):
                
                print('----old_greedy algorithm start running....')
                S=[]# seeds set
                V=[i for i in G[0]]# candidated seeds set
                
                #------------------------valadite-------------------------------
                # Topic=T[0]
                # TK=self.TJk[self.TJts.index(Topic)]
                #---------------------------------------------------------------
                
                for i in range(K):# seeds set num: K
                        print('### start selecting the ',i,'th seed ...')
                        
                        time1=now()
                        max_sv=0
                        max_v=-1
                        
                        for v in V:
                                # print('********************************************',v)
                                SS=[]
                                SS=[j for j in S]
                                SS.append(v)
                                sv=0
                                
                                for j in range(self.ROUND):# num of simulations
                                        time11=now()
                                        sv+=lis.labeled_influence_spread_S(SS,G,T)# one simulations
                                        time22=now()
                                        # print('^^^^^this round takes :',time22-time11,' s .. ^^^^^')
                                sv=sv/self.ROUND
                                
                                if max_sv<sv:
                                        max_sv=sv
                                        max_v=v
                                        
                                # if v in TK:
                                        # print('---TJ--',v,':',sv,'ADJ=',len(G[3][v]),'---')
                                        
                        S.append(max_v)
                        V.remove(max_v)
                        time2=now()
                        print('%%% A seed is added: ',max_v,'. %%% Total Neighbors is ',len(G[3][max_v]),'. %%% Total profit is ',max_sv,'\n this seed selection takes ',time2-time1,' s')
                print('----greedy algorithm end running.')
                return S