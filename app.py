import pandas as pd
import streamlit as st
import plotly.express as px

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

# Step 3 - Column filter
st.header('')
st.subheader("1. Select a Column")
default_cols = ["Name", "Sex", "Survived", "Age"]
cols = st.multiselect("Columns", df.columns.tolist(), default = default_cols)
st.dataframe(df[cols].head(100))

##########################
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

# Step 5 - Distributions 
st.header('')
st.subheader('3. Select a range of Age within the sidebar')
values = (st.sidebar.slider("Price Range", float(df.Age.min()), float(df.Age.clip(upper=100.).max()), (0., 100.)))
hist = px.histogram(df.query(f"Age.between{values}", engine='python'), x="Age", nbins=10, title = "Age Distribution")
hist.update_xaxes(title="Age")
hist.update_yaxes(title="# of People")
st.plotly_chart(hist)

# Step 6 - Radio Buttons
st.header('')
st.subheader('4. Select a range of Age within the sidebar')
col1, col2 = st.columns(2)
with col1:
    Rclass = st.radio("Pclass", df.Pclass.unique())
with col2:
    RSex = st.radio("Sex", df.Sex.unique())