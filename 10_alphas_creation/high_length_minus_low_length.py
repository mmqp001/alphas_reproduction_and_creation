#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    high_length_minus_low_length=dv.add_formula('high_length_minus_low_length','Ts_Argmax(high,%s)-Ts_Argmin(low,%s)'%(20,20),is_quarterly=False)
    
    return high_length_minus_low_length