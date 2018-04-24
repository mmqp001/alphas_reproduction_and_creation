
# coding: utf-8

# In[ ]:


#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    NOCFToOperatingNILatest=dv.add_formula('NOCFToOperatingNILatest','net_cash_flows_oper_act/(total_oper_rev-tot_oper_cost)',is_quarterly=False)
    return NOCFToOperatingNILatest

