#type3  -  the intermediate variable of the factor is also a factor

def interval_mean(Df,n):
    import numpy as np
    Df_mean=Df.rolling(n).mean().iloc[::n]
    Df_copy=Df.copy()
    Df_copy.loc[:,:]=np.nan
    Df_copy.loc[Df_mean.index]=Df_mean
    Df_copy=Df_copy.fillna(method='ffill')
    #注意这里要用ffill不能用bfill，用bfill就用到未来值了
    return Df_copy

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Hur=dv.add_formula('Hur','Ts_Sum(close-interval_mean(close,%s),%s)'%(t,t),is_quarterly=False,register_funcs={'interval_mean':interval_mean})
    
    return Hur