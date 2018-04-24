#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    volume_diff=dv.add_formula('volume_diff','Delta(volume,1)',is_quarterly=False,add_data=True)
    volume_ratio=dv.add_formula('volume_ratio','Ts_Sum((Abs(volume_diff)+volume_diff)/2,%s)/Ts_Sum((Abs(volume_diff)-volume_diff)/2,%s)'%(t,t),is_quarterly=False)
    
    return volume_ratio