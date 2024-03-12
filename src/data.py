from libraries import pd,os
import pathlib


PATH=pathlib.Path(__file__).parent
DATA_PATH=PATH.joinpath("data/gulf_df.csv").resolve()


### importing final file exported from  wrangling process
gulf_df=pd.read_csv(DATA_PATH)
df=gulf_df.drop(columns="Unnamed: 0",axis=1)

######### lists used
gulf_countries=['Saudi Arabia','United Arab Emirates',"Kuwait","Bahrain","Oman","Qatar","Iraq",] #country_list
diseases_list=gulf_df["cause"].unique().tolist()

