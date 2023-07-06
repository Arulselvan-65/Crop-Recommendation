import streamlit as st
import pandas as pd
import csv
import altair as at
import plotly.express as px

## 00589C   016FC4   1891C3  3AC0DA   3DC6C3   50E3C2
hide = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
@st.cache_data
def filter_crop(csv_file, fr_yr, to_yr, dist, crp_lst):
    crop_list = crp_lst
    filtered = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if fr_yr <= row['year'] <= to_yr and row['Dis'] == dist and row['crop'] in crop_list:
                filtered.append((row['year'], float(row['prod']), row['crop']))
    return filtered
@st.cache_data
def get_crops(csv_file, dis_name, fr_yr, to_yr):
    dis_crops = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if fr_yr <= row['year'] <= to_yr and row['Dis'] == dis_name:
                dis_crops.append(row['crop'])
    return dis_crops
st.set_page_config(
    page_title="Crop Data",
    page_icon=":shamrock:",
    initial_sidebar_state="auto",
)
st.markdown(hide,unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        text-align: center;
        padding-top: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("<h1 class='title'>Crop Production Data</h1>", unsafe_allow_html=True)

st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")

from_year = st.selectbox("From",
                         ['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                          '2009',
                          '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
st.write("\n\n\n")
to_year = st.selectbox("Till",
                       ['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
st.write("\n\n\n")
dis_val = st.selectbox("District",
                       ['Ariyalur', 'Chengalpattu', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul',
                        'Erode',
                        'Kallakurichi', 'Kanchipuram', 'Kanniyakumari', 'Karur', 'Krishnagiri', 'Madurai',
                        'Nagapattinam', 'Namakkal',
                        'Perambalur', 'Pudukkottai', 'Ramanathapuram', 'Ranipet', 'Salem', 'Sivaganga', 'Tenkasi',
                        'Thanjavur', 'The Nilgiris',
                        'Theni', 'Thiruvallur', 'Thiruvarur', 'Thoothukudi', 'Tiruchirappalli', 'Tirunelveli',
                        'Tirupathur', 'Tiruppur', 'Tiruvannamalai',
                        'Tuticorin', 'Vellore', 'Villupuram', 'Virudhunagar'])

crops = sorted(list(set(get_crops("final_data3.csv", dis_val, from_year, to_year))))
st.write("\n\n\n")
crop_types = st.multiselect("Crops(maximum 4)", crops)

season_option = st.selectbox("Season", ['Kharif', 'whole_year', 'Autumn', 'Summer', 'Winter'],)
st.write("\n\n\n")

max_limit = 4
if len(crop_types) > max_limit:
    st.error(f"Please select up to {max_limit} options.")
else:
    btn_ph = st.empty()
    btn = btn_ph.button("Get Data")
    if (btn):
        if (from_year >= to_year):
            if (from_year == to_year):
                st.error("Starting and Ending Years are Same")
            else:
                st.error("Starting Year should be less than Ending Year")
        else:
            btn_ph.button("Getting data..")
            filtered_data = filter_crop("final_data3.csv", from_year, to_year, dis_val, crop_types)
            if filtered_data:
                years, prod, crops = zip(*filtered_data)
                d = {'Year': list(map(str, years)),
                     'Production(in tonnes)': list(prod),
                     'Crop': list(crops)}
                df = pd.DataFrame(d)
                color_sequence = ['#8EA7E9','#607EAA', '#1E56A0', '#163172']
                st.write("\n\n\n")
                st.write("\n\n\n")
                st.write("\n\n\n")
                bar_chart = at.Chart(df).mark_bar().encode(
                    x="Year:O",
                    y="Production(in tonnes):Q",
                    color= at.Color("Crop:N" ,scale=at.Scale(range=color_sequence)),
                ).properties(
                    width=at.Step(20),
                    height=400).configure_view(
                    stroke=None
                )
                title = f"<h2 style='text-align: center; font-weight: bold;'>Yearly Production of Crops in {dis_val}<br>between {from_year} to {to_year}</h2>"
                st.markdown(title, unsafe_allow_html=True)
                st.write ("\n\n\n")
                st.write ("\n\n\n")
                st.altair_chart(bar_chart, use_container_width=True)


                crop_production = {}
                for crop_name in crops:
                    filtered_data = df[df['Crop'] == crop_name]
                    total_production = filtered_data['Production(in tonnes)'].sum()
                    crop_production[crop_name] = total_production

                val = list(crop_production.keys())
                sizes = list(crop_production.values())

                val, sizes = zip(*sorted(zip(val, sizes), key=lambda x: x[1], reverse=True))

                data = dict(
                    Production=val,
                    sizes=sizes
                )
                st.write("\n\n\n")
                st.write("\n\n\n")
                st.write("\n\n\n")
                tit = f"<h2 style='text-align: center; font-weight: bold;'>Total Production of Crops in {dis_val}<br>between {from_year} to {to_year}</h2>"
                st.markdown(tit, unsafe_allow_html=True)
                color_sequence1 = ['#163172', '#1E56A0','#607EAA','#8EA7E9']
                fig = px.pie(df,names = data['Production'],values = data['sizes'],hole=.3,color=data['Production'],color_discrete_sequence = color_sequence1)
                fig.update_layout (autosize=False,width=500,height=500,legend=dict(font=dict(size=10)))
                st.plotly_chart(fig,use_container_width=True)

            else:
                st.error(
                    "No records found for the Selected Crop.Consider selecting Different Crop or the range of Years.")

        btn_ph.button("Get Data", key=btn)
