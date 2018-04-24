#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
        
    t = param['t']
    
    LCAPHist120=dv.add_formula('LCAPHist120','%s*pb/Ts_Sum(LCAP,%s)'%(t,t),is_quarterly=False)
    
    return LCAPHist120