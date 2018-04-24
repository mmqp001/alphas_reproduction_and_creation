
# coding: utf-8

# In[1]:


#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Illiquidity=dv.add_formula('Illiquidity','Ts_Sum(close/Delay(close,1)-1,%s)/Ts_Sum(turnover,%s)*Pow(10,9)'%(t,t),is_quarterly=False)
    
    return Illiquidity

