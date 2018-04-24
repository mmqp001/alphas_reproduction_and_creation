#type3  -  the intermediate variable of the factor is also a factor

def sum_axis1(Df):
    sum_1=Df.sum(axis=1)
    Df_copy=Df.copy()
    Df_copy.loc[sum_1.index,:]=sum_1.values.reshape(-1,1)
    return Df_copy

def run_formula(dv, param = None):
    defult_param = {'t':4}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Factor1=dv.add_formula('Factor1','Rank(Delta(((high*close/sum_axis1(close)) + (vwap *(1-close/sum_axis1(close)))), %s) )'%(t),is_quarterly=False,register_funcs={'sum_axis1':sum_axis1})

    return Factor1