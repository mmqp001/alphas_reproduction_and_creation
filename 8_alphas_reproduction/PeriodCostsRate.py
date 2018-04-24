
# coding: utf-8

# In[ ]:


#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    PeriodCostsRate=dv.add_formula('PeriodCostsRate','(fin_exp+less_selling_dist_exp+less_gerl_admin_exp)/oper_rev',is_quarterly=False)
    return PeriodCostsRate

