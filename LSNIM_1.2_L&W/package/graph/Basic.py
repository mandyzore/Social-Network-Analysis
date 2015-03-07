#coding=utf-8


def get_ADJ(G,d):
        ADJ=[[] for i in range(len(G[0]))] #node
        
        if d=='dir': 
                for i in G[1]:#E=edge[eid nid1 nid2]
                        nid1=i[1]
                        nid2=i[2]
                        if nid2 not in ADJ[nid1]:
                                ADJ[nid1].append(nid2)# not exist
                                
        elif d=='undir':
                for i in G[1]:#E=edge[eid nid1 nid2]
                        nid1=i[1]
                        nid2=i[2]
                        if nid2 not in ADJ[nid1]:
                                ADJ[nid1].append(nid2)# not exist
                        if nid1 not in ADJ[nid2]:
                                ADJ[nid2].append(nid1)# not exist
        return ADJ

def get_adj(v,G,d):
        adj_v=[]
        E=G[1]# eid nid1 nid2
        clock=0
        
        if d=='dir':
                for i in E:
                        if int(i[1])==int(v):
                                adj_v.append(i[2])
                                clock+=1
                        elif clock!=0:
                                break
                        elif clock==0:
                                continue
                        else:
                                print('!!!wrong!!!')
        elif d=='undir':
                for i in E:
                        if int(i[1])==int(v):
                                adj_v.append(i[2])
                        elif int(i[2])==int(v):
                                adj_v.append(i[1])
                        else:
                                print('!!!wrong!!!')
        return adj_v
        
def get_degree(v,G):
        d=0
        return d
        
def get_langest_edge(G):
        length=0
        chain=[]
        # for 
        
        return chain