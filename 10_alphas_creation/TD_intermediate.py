#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':6}
    if not param:
        param = defult_param
        
    t = param['t']
    
    TD_intermediate=dv.add_formula('TD_intermediate','If(high>=Ts_Min(low,%s) && low<=Ts_Max(high,%s),high-Ts_Max(high,%s)+low-Ts_Min(low,%s),0)'%(t,t,t,t),is_quarterly=False)
    
    return TD_intermediate