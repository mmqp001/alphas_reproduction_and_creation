#type3  -  the intermediate variable of the factor is also a factor

def sum_axis1(Df):
    sum_1=Df.sum(axis=1)
    Df_copy=Df.copy()
    Df_copy.loc[sum_1.index,:]=sum_1.values.reshape(-1,1)
    return Df_copy

def SMA(Df,n,m):
    alpha=m/n
    return Df.ewm(alpha=alpha,adjust=False).mean()

def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':2}
    if not param:
        param = defult_param
        
    t1 = param['t1']
    t2 = param['t2']
    
    crosssec_weight_vc=dv.add_formula('crosssec_weight_vc','SMA(volume,%s,%s)/sum_axis1(SMA(volume,%s,%s))*SMA(close,%s,%s)/sum_axis1(SMA(close,%s,%s))'%(t1,t2,t1,t2,t1,t2,t1,t2),is_quarterly=False,register_funcs={'SMA':SMA,'sum_axis1':sum_axis1})
    
    return crosssec_weight_vc