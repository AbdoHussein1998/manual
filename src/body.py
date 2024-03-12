from libraries import dcc,html,Dash,go
import data
import ids
import fun
image_path = 'assets/WHO_logo.png'

def mainbody ():
    app=Dash(__name__)
    app.layout=html.Div(id=ids.main_div,className="main_div",children=[
        html.Div(id=ids.imgcompo,children=[
                                            html.H1(id=ids.title_H1,className="title_H1",children=["Total deaths in Arabic gulf countries by WHO "],style={"text-align":"center"}),
                                            html.Img(src=image_path,alt="WHO logo",width=50,height=50),
                                           ]),
        html.Div(id=ids.div_dropdown,children=[
                                                html.Div(id=ids.div_dropdown_diseases,children=[dcc.Dropdown(id=ids.dropdown_diseases,options=data.diseases_list,value=["Mental Disorders"],multi=True,searchable=True,clearable=True,placeholder="Select the diseases you want....",className="dropdown_diseases",),
                                                html.Button(id=ids.all_dis_butt,children=["All diseases"],n_clicks=0),]),
                                                html.Br(),
                                                html.Div(id=ids.div_dropdown_countries,children=[dcc.Dropdown(id=ids.dropdown_countries,options=data.gulf_countries,value=["Qatar"],multi=True,searchable=True,clearable=True,placeholder="Select the countries you want...."),
                                                html.Button(id=ids.all_coun_butt,children=["All countries"],n_clicks=0),]),
                                                html.Br(),
        ]),

        html.Div(id=ids.graph_div,children=[dcc.Graph(id=ids.main_graph,figure=go.Figure())]),
        html.Br(),
        html.H5(id=ids.H6_note,className="H6_note",children=["Note: these data were pulled only form World Health Organization"]),
    ])
            
    return app

