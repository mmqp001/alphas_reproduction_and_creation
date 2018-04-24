
# coding: utf-8

# In[1]:


#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
        
    t = param['t']
    
    PEHist120=dv.add_formula('PEHist120','%s*pe/Ts_Sum(pe,%s)'%(t,t),is_quarterly=False)
    
    return PEHist120

