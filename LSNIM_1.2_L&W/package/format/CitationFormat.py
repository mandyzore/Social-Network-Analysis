#coding=utf-8

import string
from time import clock as now
import platform
# 0 Topic 16: Data Mining / Association Rules
# 1 Topic 107: Web Services, 
# 2 Topic 131: Bayesian Networks / Belief function, 
# 3 Topic 144: Web Mining / Information Fusion,
# 4 Topic 145: Semantic Web / Description Logics, 
# 5 Topic 162: Machine Learning, 
# 6 Topic 24: Database Systems / XML Data, 
# 7 Topic 75: Information Retrieval, 
# 8 Topic 182: Pattern recognition / Image analysis, 
# 9 Topic 199: Natural Language System / Statistical Machine Translation. 

class CF:
        #格式化Citation数据
        
        NODE=2555
        EDGE=6101
        TOPIC=10
        topics=['0','1','2','3','4','5','6' ,'7','8','9']
        
        PATH_SUBS=''
        PATH_OUT=''
        
        # PATH_SUBS='/data/Citation/1/'
        # PATH_OUT='/data/bean/Citation/'
        
        PATH=''
        PATH_M=''
        
        def __init__(self,p):
                if platform.system()=='Linux':
                        self.PATH_M='/'
                elif platform.system()=='Windows':
                        self.PATH_M='\\'
                        
                self.PATH_SUBS=self.PATH_M.join(['data','Citation','1'])
                self.PATH_OUT=self.PATH_M.join(['data','bean','Citation'])
                
                print('self.PATH_SUBS:',self.PATH_SUBS)
                print('self.PATH_OUT:',self.PATH_OUT)
                
                self.PATH=p
                
                print('class CitationFormat init...')
                

        #文件列表合并--基于话题的边
        def get_topic_merge(self):
                ptns=[]
                ptes=[]
                biP=[]
                # nfp='node/ '
                # efp='edge/ '
                nfp='node'
                efp='edge'
                
                tff=[[0,0] for i in range(10)]
                for tf in self.topics:#遍历每个topic文件   
                        
                        #1.node################ citation
                        ptn=[]
                        f_in_n=open(self.PATH+self.PATH_M+self.PATH_SUBS+self.PATH_M+nfp+self.PATH_M+'n'+tf+'.net','r')
                        for line in f_in_n.readlines():#遍历每行
                                line=line.strip('\n')
                                line=line.replace('\t"','\t')#文章标题去掉引号
                                line=line.replace('"\t','\t')
                                s=line.split('\t')
                                ss=[s[0],s[1],s[2],str(tf)]#添加话题编号
                                ptn.append(ss)
                                tff[int(tf)][0]+=1
                        ptn=sorted(ptn,key= lambda x:int(x[0]))#[tpid title citation topicid]
                        f_in_n.close()
                        ptns.extend(ptn)#[[tpid title citation topicID]] node
                        # print('topic-',tf,' node=',len(ptn))
                        
                         #2.edge################
                        pte=[]
                        f_in_e=open(self.PATH+self.PATH_M+self.PATH_SUBS+self.PATH_M+efp+self.PATH_M+'e'+tf+'.net','r')
                        for line in f_in_e.readlines():#遍历每行
                                s=line.split()# pid1 pid2 0
                                ss=[ptn[int(s[0])][1],ptn[int(s[1])][1],str(tf)]# title1 title2 topicid
                                pte.append(ss)
                                tff[int(tf)][1]+=1
                        # print('topic-',tf,' edge=',len(pte))
                        f_in_e.close()
                        ptes.extend(pte)#[[title1 title2 topicID]] edge
                print('node ptns:',len(ptns),'edge ptes:',len(ptes))
                
                #检查
                ttfn=0
                ttfe=0
                for i in tff:
                        ttfn+=i[0]
                        ttfe+=i[1]
                print('total count: node=',ttfn,' edge=',ttfe)
                bip=[ptns,ptes]
                
                #############################
                # print('$$$$$$$$$$$$$$$$$$$$$:  ',ptns[0])
                fo1=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'ptns.bean','w')
                for l in ptns:
                        ll=''
                        ll='\t'.join(l)
                        fo1.write(ll+'\n')
                        # print('ptns:',ll)
                fo1.close()
                
                fo2=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'ptes.bean','w')
                for l in ptes:
                        ll=''
                        ll='\t'.join(l)
                        fo2.write(ll+'\n')
                fo2.close()
                #############################
                return bip

        def get_pid_title(self,all_fp):# nid title year venue authors (5)
                f_in=open(all_fp)#所有文章node总索引
                titles=''
                for line in f_in.readlines():
                        line=line.strip('\n')
                        ls=line.split('\t')
                        title=ls[1]
                        titles=titles+title+'$'
                titles=titles.split('$')
                
                ## print('*********titles.pop():'+titles.pop())
                return titles #titles list

        def get_node_with_topic(self,titileIndex,ptns,ptes):
                ptopics=[]# the distribuation of 2555 papers on 10 topics. the citation represent the weight
                
                for i in range(self.NODE):#2555
                                ptopics.append([i,[0 for j in range(self.TOPIC)]])
                
                
                print('titileIndex:',len(titileIndex))
                print('ptopics:',len(ptopics))
                
                for p in ptns:#[[tpid title citation topicID]] node--2660
                        title=p[1]
                        topicid=int(p[3])
                        # citation=int(p[2])
                        pid=titileIndex.index(title)#文章id
                        ptopics[pid][1][topicid]=1# 文章所属话题分类


                for e in ptes:#[[title1 title2 topicID]] edge-all 6101
                        title=e[1]## reverse the edge !!!
                        topicid=int(e[2])
                        pid=titileIndex.index(title)#文章id
                        ptopics[pid][1][topicid]+=1#文章在此话题中的引用得分
                
                 
                return ptopics #[[nid topicScore[]] 
                
        def get_edge_with_topic(self,titileIndex,ptes):
                
                epid=[]
                print('*************************** ptes=',len(ptes))
                for p in ptes:# [[title1 title2 topicID]] edge
                        ep=[]
                        ep=[titileIndex.index(p[1]),titileIndex.index(p[0]),p[2]]# [[pid1 pid2 topicID]] edge--> reverse!!
                        epid.append(ep)
                epid=sorted(epid,key = lambda x:( int(x[0]),int(x[1]),int(x[2]) ) )# nid1 nid2 topic--6101
                print('*************************** epid=',len(epid))
                
                # [eid nid1 nid2 topicID[]]
                epidd=[]
                edge=[]
                eid=0
                count=0
                for p in epid:# nid1 nid2 topic--6101
                        tt=[0 for i in range(10)]
                        ep=[]
                        tmpe=[p[0],p[1]]
                        
                        if edge!=tmpe:# 1.a new edge
                                tt[int(p[2])]+=1
                                ep=[eid,p[0],p[1],tt]# eID nID1 nID2 topicID[]
                                epidd.append(ep)
                                eid+=1
                                edge=tmpe
                        elif edge==tmpe:# 2.the same edge with a different topic
                                count+=1
                                epidd[eid-1][3][int(p[2])]+=1
                        else :
                                print('!!!!!!!!!! WRONG EDGE !!!!!!!!!!!!!')
                                print(p)
                # print('重复边：',count) #134
                return epidd # [eid nid1 nid2 topicID[]]
                
        #Data Bean
        def set_bean(self):
                
                gfp=self.PATH+self.PATH_M+self.PATH_SUBS+self.PATH_M+'node'+self.PATH_M+'all_node.dat'
                
                #[[tpid title citation topicID]] node
                #[[title1 title2 topicID]] edge 
                [ptns,ptes]=self.get_topic_merge()
                
                ti=self.get_pid_title(gfp)#[[nid title]] node
                pt=self.get_node_with_topic(ti,ptns,ptes) # [nid,topicScore[]] node
                
                
                
                ##检查验证
                # node
                ts=[0,0,0,0,0,0,0,0,0,0]
                for i in pt:
                        for j in range(10):
                                ts[j]=ts[j]+i[1][j]

                print('检查验证:',ts)
                tss=0
                for i in ts:
                        tss=tss+i
                print('tss:',tss)
                
                # write node bean
                f_out=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'citation_node_topicDistribution.bean','w')
                
                for l in pt:#[[nid topicScore[]]] node
                        ts='\t'.join([str(i) for i in l[1]])
                        ll=str(l[0])+'$'+ts
                        f_out.write(ll+'\n')
                f_out.close()

                # write edge bean
                epid=self.get_edge_with_topic(ti,ptes)
                fo=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'citation_edge_topicDistribution.bean','w')
                
                for l in epid:# [eID nID1 nID2 topicID[]]
                        ts='\t'.join([str(i) for i in l[3]])
                        ll=str(l[0])+'\t'+str(l[1])+'\t'+str(l[2])+'$'+ts
                        fo.write(ll+'\n')
                fo.close()
                
        def get_bean(self,str):
                if str=='node':
                        fi=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'citation_node_topicDistribution.bean','r')
                        nt=[]
                        for i in fi.readlines():# [nID $ topicID[]]
                                s=i.split('$')
                                nid=int(s[0])
                                ts=s[1].split('\t')
                                tss=[int(j) for j in ts]
                                nt.append([nid,tss])
                        fi.close()
                        return nt
                        
                if str=='edge':
                        fi=open(self.PATH+self.PATH_M+self.PATH_OUT+self.PATH_M+'citation_edge_topicDistribution.bean','r')
                        et=[]
                        for i in fi.readlines():# [eID nID1 nID2 $ topicID[]]
                                s=i.split('$')
                                s1=s[0].split('\t')
                                s2=s[1].split('\t')
                                ss2=[int(j) for j in s2]
                                et.append([int(s1[0]),int(s1[1]),int(s1[2]),ss2])
                        fi.close()
                        return et
                        
##########################################################################################
if __name__ == '__main__':
        cf=CF()
        cf.set_bean()
        