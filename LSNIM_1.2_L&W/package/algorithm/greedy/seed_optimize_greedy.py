#coding=utf-8

# import sys
# sys.path.append('..')
# print(sys.path)

from time import clock as now




class SOG:
        
        #step1: calculate edge
        #step2: define weak edge
        #step2: remove weak edge
        #step3: region adjust
        #step4: seed selection
        #step5: 
        
        
        
        ROUND=0
        
        def __init__(self,round):
                self.ROUND=round
                print('old_greedy init...')
        

        def run(self,G,K,T,lIS):
                print('----greedy algorithm start running....')
                S=[]# seeds set
                
                for i in range(K):# seeds set num: K
                        print('### start selecting the ',i,'th seed ...')
                        
                        time1=now()
                        max_sv=0
                        max_v=-1
                        V=G[0]
                        for v in V:
                                # print('## node ',v,'’  propagation...')
                                
                                sv=0
                                for j in range(self.ROUND):# propagate step deepth:ROUND
                                        sv+=lIS.labeled_influence_spread(v,G,T)# one step
                                sv=sv/self.ROUND
                                if sv>max_sv:
                                        max_sv=sv
                                        max_v=v
                        S.append(max_v)
                        V.remove(max_v)
                        time2=now()
                        print('%%% A seed is added: ',max_v,'. %%% Total profit is ',max_sv,'\n this seed selection takes ',time2-time1,' s')
                print('----greedy algorithm end running.')
                return S
