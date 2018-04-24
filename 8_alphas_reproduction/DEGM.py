
# coding: utf-8

# In[ ]:


#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    DEGM=dv.add_formula('DEGM','(oper_rev-less_oper_cost)/oper_rev-Delay((oper_rev-less_oper_cost)/oper_rev,365)',is_quarterly=False)
    return DEGM 

