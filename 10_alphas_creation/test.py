
# coding: utf-8

# In[17]:


import pandas as pd


def get_dv(start = 20170101,end = 20180101): 
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService
    
    import warnings
    warnings.filterwarnings("ignore")
    
    #--------------------------------------------------------
    
    #define
    factor_list = ['turnover','ETOP','LCAP','volume']
    check_factor = ','.join(factor_list)
    
    dataview_folder='G:\GSICE\DATA\data'
    ds = LocalDataService(fp = dataview_folder)
    
    ZZ800_id = ds.query_index_member("000906.SH", start, end)
    stock_symbol = list(set(ZZ800_id))
    
    dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
             'fields': check_factor,
             'freq': 1,
             "prepare_fields": True}
    
    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()
    
    data_config = {
    "remote.data.address": "tcp://data.tushare.org:8910",
    "remote.data.username": "13662241013",
    "remote.data.password": "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MTc2NDQzMzg5MTIiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM2NjIyNDEwMTMifQ.sVIzI5VLqq8fbZCW6yZZW0ClaCkcZpFqpiK944AHEow"
    }
    
    from jaqs_fxdayu.data import RemoteDataService
    Ds=RemoteDataService()
    Ds.init_from_config(data_config)
    dv.add_field('pb',Ds)
    dv.add_field('ps',Ds)
    
    return dv


# In[18]:


if 'dv' not in dir():
    dv = get_dv()


# In[19]:


#--------------------------------------------------------- 
#test output
def test(factor,data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date','report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
        
        if columns_dtype not in ['object','str']:
            raise TypeError('error columns type')
            
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')
        print ('{} OK!'.format(factor))

import PBHist120,turnover_mean20_sd,high_length_minus_low_length,volume_ratio,ETOPHist120,TD_intermediate,psHist120,Hur,close_ratio,LCAPHist120,crosssec_weight_vc,Factor1,Factor2

for f in ['PBHist120','turnover_mean20_sd','high_length_minus_low_length','volume_ratio','ETOPHist120','TD_intermediate','psHist120','Hur','close_ratio','LCAPHist120','crosssec_weight_vc','Factor1','Factor2']:
    test(f, globals()[f].run_formula(dv))

