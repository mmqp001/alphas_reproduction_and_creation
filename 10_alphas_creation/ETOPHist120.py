#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
        
    t = param['t']
    
    ETOPHist120=dv.add_formula('ETOPHist120','%s*pb/Ts_Sum(ETOP,%s)'%(t,t),is_quarterly=False)
    
    return ETOPHist120