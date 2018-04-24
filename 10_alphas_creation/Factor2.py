#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':5}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Factor2=dv.add_formula('Factor2','If(volume>Delay(volume,%s),Ts_Max(high,%s),Ts_Min(low,%s))'%(t,t,t),is_quarterly=False)

    return Factor2



