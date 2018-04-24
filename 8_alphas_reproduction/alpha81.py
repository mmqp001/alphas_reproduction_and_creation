
# coding: utf-8

# In[1]:


def SMA(Df,n,m):
    alpha=m/n
    return Df.ewm(alpha=alpha,adjust=False).mean()


# In[3]:


#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t1':21,'t2':2}
    if not param:
        param = defult_param
        
    t1 = param['t1']
    t2 = param['t2']
    
    alpha81=dv.add_formula('alpha81','SMA(volume,%s,%s)'%(t1,t2),is_quarterly=False,
      register_funcs={'SMA':SMA})
    
    return alpha81

