import os
import string
from format import CitationFormat
from format import MovieFormat
PATH=''


# print(PATH)
p=os.path.realpath(__file__)
ps=p.split('\\')
ps.pop()
ps.pop()
PATH='\\'.join(ps)
# print(fp1)

# fp2=os.path.split(os.path.realpath(__file__))[0]
# print(fp2)

##############################
cf=CitationFormat.CF(PATH)
# print('then...')
# cf.set_bean()
# nt=cf.get_bean()
# et=cf.get_bean()


##############################
mf=MovieFormat.MF(PATH)
print('then...')
node=mf.load_node()
edge=mf.load_edge()

for i in range(20):
    print(mf.EXTRA_TOPICS[i])

##et=mf.filter_extra_topics()





