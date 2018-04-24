#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    turnover_mean20=dv.add_formula('turnover_mean20','Ts_Mean(turnover,%s)'%(t,),is_quarterly=False,add_data=True)
    turnover_mean20_sd=dv.add_formula('turnover_mean20_sd','(turnover_mean20-Ts_Min(turnover_mean20,%s))/(Ts_Max(turnover_mean20,%s)-Ts_Min(turnover_mean20,%s))'%(t,t,t),is_quarterly=False)
    
    return turnover_mean20_sd