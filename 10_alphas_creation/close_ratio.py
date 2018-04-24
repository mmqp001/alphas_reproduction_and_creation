#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    close_diff=dv.add_formula('close_diff','Delta(close,1)',is_quarterly=False,add_data=True)
    close_ratio=dv.add_formula('close_ratio','Ts_Sum((Abs(close_diff)+close_diff)/2,%s)/Ts_Sum((Abs(close_diff)-close_diff)/2,%s)'%(t,t),is_quarterly=False)
    
    return close_ratio