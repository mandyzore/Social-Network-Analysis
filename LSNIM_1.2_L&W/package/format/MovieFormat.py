#coding=utf-8

import string
from time import clock as now
import platform

class MF:
        #格式化Citation数据
        
        NODE=34283
        EDGE=142427
        TOPIC=10
        TYPE=4
        TYPES=['starring','writer','director','movie']
        TOPICS=['American film actors', 'American television actors', 'Black and white films', 'Drama films', 'Comedy films', 'British films', 'American film directors', 'Independent films', 'American screenwriters', 'American stage actors']
        
        # PATH_IN='\\data\\Movie\\'
        # PATH_OUT='\\data\\bean\\Movie\\'
        PATH_IN=''
        PATH_OUT=''
        
        PATH=''#LISM[doc,pakage[format],source[raw,bean],result]
        PATH_M=''
        
        def __init__(self,p):
                
                if platform.system()=='Linux':
                        self.PATH_M='/'
                elif platform.system()=='Windows':
                        self.PATH_M='\\'
                        
                self.PATH_IN=self.PATH_M.join(['data','Movie'])
                self.PATH_OUT=self.PATH_M.join(['data','bean','Movie'])
                
                self.PATH=p
                print('class MovieFormat init...')
                
        def filter_extra_topics(self):
                # et=sorted(self.EXTRA_TOPICS)
                et=[]
                for i in self.EXTRA_TOPICS:
                        try:
                                et.index(i)
                        except ValueError:
                                et.append(i)
                return et
                
        #NODE
        def load_node(self):
                print('strat load_node...')
                node=[]
                maxw=-1
                fi=open(self.PATH+self.PATH_M+self.PATH_IN+self.PATH_M+'node.txt','r')
                for line in fi.readlines():
                        if line.strip()!='':
                                l=line.split('\t')#[id,name,weight,type,topics]
                                #fill with types id
                                l[3]=self.TYPES.index(l[3])
                                #fill with topics id
                                t=l[4].split(';')
                                tt=[0 for i in range(10)]
                                for i in t:
                                        if i in self.TOPICS:
                                                tt[self.TOPICS.index(i)]=1
                                                
                                s=[int(l[0]),l[1],l[2],l[3],tt]#[nid,name,weight,type,topicID]
                                node.append(s)
                                #maxweight
                                if maxw<int(l[2]):
                                        maxw=int(l[2])
                print('end load_node.',len(node))
                ##print('max weight:',maxw)
                return node
                
        def load_edge(self):
                print('strat load_edge...')
                edge=[]
                fi=open(self.PATH+self.PATH_M+self.PATH_IN+self.PATH_M+'edge.txt','r')
                for line in fi.readlines():
                        if line.strip()!='':
                                l=line.split('\t')#[nid1,nid2,1]
                                #fill with types id
                                edge.append([int(l[0]),int(l[1])])#[nid1,nid2]
                                
                print('end load_node.',len(edge))
                edge=sorted(edge,key= lambda x:(int(x[0]),int(x[1])))
                        
                edge_DeRe=[]
                eid=0                        
                ee=[]
                for e in edge:# nid1 nid2 topic--6101
                        
                        tmpe=[e[0],e[1]]
                        if ee!=tmpe:# 1.a new edge
                                edge_DeRe.append([eid,e[0],e[1]])
                                eid+=1
                                ee=tmpe
                        elif ee==tmpe:# 2.the same edge with a different topic
                                continue
                        else :
                                print('!!!!!!!!!! WRONG EDGE !!!!!!!!!!!!!')
                                print(p)
                
                print('reduce edge:',len(edge)-len(edge_DeRe),' new:',len(edge_DeRe))
                
                return edge_DeRe
                
        def get_node_by_type(self,node):
                n=[]
                star=[]
                writer=[]
                director=[]
                movie=[]
                
                for i in node:
                        if i[2]=='starring':
                                star.append(i)
                        elif i[2]=='writer':
                                writer.append(i)
                        elif i[2]=='director':
                                director.append(i)
                        elif i[2]=='movie':
                                movie.append(i)
                                
                n=[star,writer,director,movie]
                return n
                