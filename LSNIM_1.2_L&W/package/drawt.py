from matplotlib.pyplot import *
import numpy as np
      
fig=figure(  )
z=np.random.randn( 10 )
      
subplot( 211 )
pla,=plot(z,"ro",ms=10,mfc="r",mew=2,mec="r") # red filled circle
plb,=plot( z[:5],"w+",ms=10,mec="w",mew=2) #while cross
legend( [pla,( pla,plb )],["Attr A","Attr A+B"] )
      
subplot( 212 )
plot( [1,2,3],label="test1" )
plot( [3,2,1],label="test2" )
legend( loc=2,borderaxespad=0. )
      
fig.savefig( "legends" )
fig.show(  )