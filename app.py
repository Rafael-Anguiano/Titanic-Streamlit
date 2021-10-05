from numpy import integer
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title('Titanic Dataset with Streamlit')
st.header('Learning Streamlit')
#st.markdown("**Bold Text**")


@st.cache
def get_data():
    URL = "./train.csv"
    return pd.read_csv(URL)

df = get_data()
st.dataframe(df.head())

st.code(
    """
    @st.cache
    def get_data():
        URL = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
        return pd.read_csv(URL)
    """, language="python"
)

################################################

################################################



#------------------------Module 1--------------------------
st.header('')
st.subheader("1. Select a Column")
default_cols = ["Name", "Sex", "Survived", "Age"]
cols = st.multiselect("Columns", df.columns.tolist(), default = default_cols)
st.dataframe(df[cols].head(100))

#------------------------Module 2--------------------------
st.header('')
searched_Name = df.groupby('Name')['Name'].count()\
    .sort_values(ascending=False).index
st.markdown("### **2. Select Name:**")
select_name = []

select_name.append(st.selectbox('', searched_Name))

name_df = df[df['Name'].isin(select_name)]

col1, col2 = st.columns(2)
    
with col1:
    st.markdown(f"**Age: ** {name_df['Age'].values[0]}")
    st.markdown(f"**Fare: $** {name_df['Fare'].values[0]}")
    st.markdown(f"**Survived: ** {name_df['Survived'].values[0]}")
    
with col2:
    st.markdown(f"**Sex:** {name_df['Sex'].values[0]}")
    st.markdown(f"**Type of Class:** {name_df['Pclass'].values[0]}")

#------------------------Module 3--------------------------
st.header('')
st.subheader('3. Select a range of Age within the sidebar')
values = (st.sidebar.slider("Age Range", int(df.Age.min()), int(df.Age.clip(upper=100).max()), (0, 100)))
hist = px.histogram(df.query(f"Age.between{values}", engine='python'), x="Age", nbins=10, title = "Age Distribution")
hist.update_xaxes(title="Age")
hist.update_yaxes(title="# of People")
st.plotly_chart(hist)

#------------------------Module 4--------------------------

st.header('')
st.subheader('4. Filtering by Class, Sex, and Survived')
col1, col2 = st.columns(2)
with col1:
    Rclass = st.radio("Pclass", [1,2,3])
    RSurvived = st.radio("Survived", df.Survived.unique())
with col2:
    RSex = st.radio("Sex", df.Sex.unique())

first_filter = df[df['Pclass'] == Rclass]
first_filter = first_filter[first_filter['Survived'] == RSurvived]
first_filter = first_filter[first_filter['Sex'] == RSex]

st.dataframe(first_filter)

#------------------------Module 5--------------------------

st.header('')
st.subheader('5. Selecting quantity of columns in a Histogram')

quantity = st.sidebar.radio("Bars quantity", ['Not defined',2,3,5,9])
if quantity == 'Not defined':
  quantity = 1
hist1 = px.histogram(df.query(f"Age.between{values}", engine='python').sort_values("Age", ascending=False), x="Age", nbins=quantity-1, title = "Age Distribution").update_layout(bargap=0.1)
hist1.update_xaxes(title="Age")
hist1.update_yaxes(title="# of People")
st.plotly_chart(hist1)



# .sort_values("Age", ascending=False)


#quartile1 = df.query(f"Age.between{(0, 20)}", engine='python').groupby("Pclass").Survived.count().reset_index()
#quartile2 = df.query(f"Age.between{(21, 40)}", engine='python').groupby("Pclass").Survived.count().reset_index()
#quartile3 = df.query(f"Age.between{(41, 60)}", engine='python').groupby("Pclass").Survived.count().reset_index()
#quartile4 = df.query(f"Age.between{(61, 80)}", engine='python').groupby("Pclass").Survived.count().reset_index()



#fig = go.Figure(
#    data=[
#            go.Bar(name='First Class',  x = quartile1['Pclass'][:3], y = quartile1['Survived'][:3]),
#            go.Bar(name='Second Class', x = quartile2['Pclass'][:3], y = quartile2['Survived'][:3]),
#            go.Bar(name='Third Class', x = quartile3['Pclass'][:3], y = quartile3['Survived'][:3]),
#            go.Bar(name='61 - 80', x = quartile4['Pclass'][:3], y = quartile4['Survived'][:5])
#        ]
#)
#ig.update_yaxes(title="Survived")
#fig.update_xaxes(title="Pclass")

# Print
#st.plotly_chart(fig)


