from libraries import go,pd,ex
################ used to filtering and wrangling process  ################
def selecting_df(df,code_list,country_list):    #function to select  Dataframe based on country list and diseaes code list
    final_df=pd.DataFrame()
    if  isinstance(country_list ,list) == True:
        final_df=df.loc[df["country_name"].isin(country_list) & df["cause"].isin(code_list)]
    elif isinstance(country_list,str) == True:
        final_df=df.loc[df["country_name"].isin([country_list]) & df["cause"].isin(code_list)]
    return final_df

def selecting_country(df:pd.DataFrame,country_name:str)->pd.DataFrame: # function to select DataFrame based on country 
    final=pd.DataFrame()
    grouped =df.groupby("country_name")
    if country_name == None:
        final=pd.DataFrame()
    elif isinstance(country_name,str)==True:
        final=grouped.get_group(country_name)
    elif isinstance(country_name,list)==True:
        df_list=[]
        for i in range(0,len(country_name)):
            temp=grouped.get_group(country_name[i])
            df_list.append(temp)
        final=pd.concat(df_list)
    return final
    

def selecting_disease(df,disease_name): # function to chose dataframe based on certain diseaes
    final=pd.DataFrame()
    if disease_name==None:
        final=pd.DataFrame()
    elif isinstance(disease_name,str):
        filt=df["cause"]==disease_name
        final=df.loc[filt]
    elif isinstance(disease_name,list):
        filt=df["cause"].isin(disease_name)
        final=df.loc[filt]
    return final
 


def labling(df,code_series,): # functions to label coulmn
    temp=df.copy()
    code_list=code_series.to_list()
    for i in range(0,len(temp["cause"])):
        if temp["cause"].iloc[i] in code_list:
            temp["cause"].iloc[i]=code_series.name
    return temp





def final_filter(dataframe:pd.DataFrame,country: str,diseases:str)->pd.DataFrame:
    df=selecting_country(dataframe,country_name=country)
    df=selecting_disease(df=df,disease_name=diseases)
    df=df.rename(columns={"deaths1":"total death","country_name":"Country name","sex":"Sex"},)
    df.drop(columns="country",axis=1,inplace=True)
    df["Sex"]=df["Sex"].apply(lambda x : "Male" if x==1 else ("Female" if x ==2 else "Non-binary") )
    return df

################ used in interaction file ################
def empty_graph():
    fig=go.Figure()
    fig.update_layout(template="plotly_dark")
    return fig
    
    
    
                ################ graphing ################


def graphing(dataframe:pd.DataFrame,country: str,diseases:str)->go.Figure:
    df=final_filter(dataframe=dataframe,country=country,diseases=diseases)
    fig=ex.histogram(data_frame=df,x="year",y="total death",color="Country name",pattern_shape="Sex",)
    fig.update_layout(bargap=.2,template="plotly_dark")
    fig.update_xaxes(tickmode="linear",title="Year")
    fig.update_yaxes(title="Total deaths")
    return fig


