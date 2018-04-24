#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
        
    t = param['t']
    
    PBHist120=dv.add_formula('PBHist120','%s*pb/Ts_Sum(pb,%s)'%(t,t),is_quarterly=False)
    
    return PBHist120