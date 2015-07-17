import grass.script as grass
import os
from grass.script import raster as grassR


p=grass.mlist_grouped ('rast', pattern='*sem0*') ['PERMANENT']



for i in p:
    grass.run_command('r.to.vect', input=i, out=i+'_vect', feature='area',verbose=False, overwrite = True ) 
    grass.run_command('v.buffer', input=i+'_vect', output=i+'_vect_buffer', type='point', distance=100, overwrite=True)
    grass.run_command('v.build.all')
    grass.run_command('v.to.rast', input=i+'_vect_buffer',out=i+'_vect_buff_rast',use='attr',column='cat',overwrite=True)
    
    
    
