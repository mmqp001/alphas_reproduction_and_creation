
# coding: utf-8

# In[ ]:


#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    NetNonOIToTP=dv.add_formula('NetNonOIToTP',
                   '(plus_non_oper_rev-less_non_oper_exp)/tot_profit',
                   is_quarterly=False)
    return NetNonOIToTP

