import body
import fun
import data
import ids
from libraries import callback,Input,Output,pd,ex

@callback(Output(component_id=ids.dropdown_diseases,component_property="value"),
                 Input(component_id=ids.all_dis_butt,component_property="n_clicks"))
def all_diseaes(n_cl):
    if n_cl!=0:
        return data.diseases_list

@callback(Output(component_id=ids.dropdown_countries,component_property="value"),
                 Input(component_id=ids.all_coun_butt,component_property="n_clicks"))
def all_coun(n_cl): 
    if n_cl!=0:
        return data.gulf_countries



@callback(Output(component_id=ids.main_graph,component_property="figure"),
          Input(component_id=ids.dropdown_countries,component_property="value"),
          Input(component_id=ids.dropdown_diseases,component_property="value"))
def graph(c_va,di_value):
    if c_va==None or di_value==None :
        return fun.empty_graph()
    elif len(c_va)==0 or len(di_value)== 0:
        return fun.empty_graph()
    else:
        fig=fun.graphing(dataframe=data.df,diseases=di_value,country=c_va)
        return fig



