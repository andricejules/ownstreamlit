import streamlit as st                #pip install streamlit
import pandas as pd                   #pip install pandas
import plotly.express as px           #pip install plotly-express
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from PIL import Image  # Pillow  https://pillow.readthedocs.io/en/stable/reference/Image.html
import requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie    streamlit-lottie-0.0.3
import json


# Error
# pip install --upgrade protobuf  Per https://stackoverflow.com/a/61961016/2394542
# pip uninstall pyhton3-protobuf
# pip uninstall protobuf

# This will display the title top left of your screem
st.set_page_config(
            page_title="Web Application",
            page_icon="chart_with_upwards_trend",
            #layout="wide",
            layout="centered",
            initial_sidebar_state="expanded"
        )
# Streamlit cache things which will help to run the application faster



# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

@st.cache()

# Read the filepath 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
#lottie_coding = load_lottiefile("images/home_ani.json")
lottie_coding = load_lottiefile("images/home_ani.json")
def types(df):
    return pd.DataFrame(df.dtypes, columns=['Type'])

def main():
    st.sidebar.title("What would you like to do?")
    activities = ["Home","Exploring the data and Plotting",  "Our Team"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    # USING THE SIDE BAR
    st.sidebar.title("Please upload Your CSV File: ")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type={"csv"})   
    #uploaded_file = st.file_uploader("Choose a CSV file")
   
    #if uploaded_file is not None and choice == "Home":
    if choice == "Home":
        # My title of my project
        #st.title("Welcome To Our Web Application.")
        
        #data = pd.read_csv(uploaded_file)   cai deleted
        
        # My title of my project
        st.title("Welcome To Our Web App :rocket: ")
        st_lottie(lottie_coding, height=400, key="coding")
        
        # photo from this webpage
        # https://www.bing.com/images/search?view=detailV2&ccid=v%2foWK3YK&id=29CA8729AE68B22A3B31346DEDAE65EDD93F33AF&thid=OIP.v_oWK3YKZoBAxtORfS3g7AHaHa&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.bffa162b760a668040c6d3917d2de0ec%3frik%3drzM%252f2e1lru1tNA%26riu%3dhttp%253a%252f%252fbusinessimpactinc.com%252fwp-content%252fuploads%252f2015%252f06%252fdata_analysis.jpg%26ehk%3dTjInNsAV2U378xgrV0F8e%252byGy5aH9SJMhH%252fuiOZc2CI%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=1378&expw=1378&q=data+analysis&simid=608019596692759575&FORM=IRPRST&ck=A4E98521DEE2B3CC72781F6CF7359C8E&selectedIndex=1&ajaxhist=0&ajaxserp=0
        #IMAGE = "fotoapp.png"
        #st.markdown(
        #    """
        #   <style>
        #    .container {
        #        display: flex;
        #    }
        #    .logo-text {
        #        font-weight:1000 !impotant;
        #        font-size:60px !important;
        #        color: #f9a01b !important;
        #        padding-top: 75px !important;
        #    }
        #    .logo-img {
        #        float:center;
        #    }
        #    </style>
        #    """,
        #    unsafe_allow_html=True
        #)

        #st.markdown(
        #    f"""
        #    <div class="container">
        #        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(IMAGE, "rb").read()).decode()}">
        #        <p class="logo-text"></p>
        #    </div>
        #    """,
        #     unsafe_allow_html=True
        #)
        
       
        st.markdown(
        """
       \n
       
        """,
        #unsafe_allow_html=True,
        )
        st.subheader("About this project:")
        st.markdown('''
                  :red_circle: Users can upload a csv file.\n
                  :red_circle: The web app produces a selection menu based on the csv headers.\n
                  :red_circle: The web app can group data based on the selected column and display all group-by data.\n
                   ''')  

        st.markdown('''
                   
                   ''')  
  
    # How to get rid of "Unnamed: 0" column in a pandas DataFrame read in from CSV file?
    # https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe-    read-in-from-csv-fil
    
    elif uploaded_file is not None and choice == "Exploring the data and Plotting":

    
        #data = pd.read_csv(uploaded_file, index_col=[0])
        
        
        
        data = pd.read_csv(uploaded_file)
        
        
        
        df = data.copy()
        #all_columns = df.columns.tolist()
        st.subheader(choice)
        
        # Show dataset
        if st.checkbox("Show Dataset"):
            rows = st.number_input("Number of rows", 5, len(data))
            st.dataframe(data.head(rows))
        # Show columns
        if st.checkbox("Columns"):
            st.write(data.columns)   
        # Show Shape
        if st.checkbox("Shape of Dataset"):
            data_dim = st.radio("Show by", ("Rows", "Columns", "Shape"))
            if data_dim == "Columns":
                st.text("Number of Columns: ")
                st.write(data.shape[1])
            elif data_dim == "Rows":
                st.text("Number of Rows: ")
                st.write(data.shape[0])
            else:
                st.write(data.shape)
                
        # Show a concise summary of the dataset
        #if st.checkbox("Getting a concise summary of the dataset"):
            #st.write(data.info())
        
           # Show Data summary
        if st.checkbox("Show empty cells"):
            st.text("Datatypes Summary")
            st.write(data.isnull().sum())
            
        # Show Data summary
        if st.checkbox("Getting descriptive statistics of the data"):
            st.text("Datatypes Summary")
            st.write(data.describe())
                     
            
        if st.checkbox("Viewing the counts of categorical data and the relationship between continuous variables"):
            #type_of_plot = st.selectbox("Select Type of Plot", ["categorical data(Bar chart)","continuous data(Scatter)"])
            type_of_plot = st.selectbox("Select Type of Plot", ["categorical data(Bar chart)","continuous data(Scatter Plot)","continuous data(Heatmap)","continuous data(Histogram)"]) 
            if type_of_plot=="categorical data(Bar chart)":
                # Create a list of columns objects
                list_of_object_columns=[]
                list_of_numerical_values_columns=[] # int and float
            
                for column_name,coltype in data.dtypes.iteritems():
                    if coltype=='object':
                        list_of_object_columns.append(column_name)
                        categorical_data=list_of_object_columns
                    elif coltype=='float64' or coltype=='int64':
                        list_of_numerical_values_columns.append(column_name)
                        numerical_data=list_of_numerical_values_columns  
                        
                column = st.selectbox("Pick an item : ",list_of_object_columns) 
                fig=plt.figure(figsize=(10,4))
                sns.countplot(x=column,data=data)
                st.pyplot(fig)
                #st.write("Bar Plot")
                #x_column1 = st.selectbox("Select a column for X Axis", categorical_data)
                #st.write(sns.catplot(x="color",data=data,kind="count", aspect=1.5))
                
        
            elif type_of_plot=="continuous data(Scatter Plot)":
                # Create a list of columns objects
                list_of_object_columns=[]
                list_of_numerical_values_columns=[] # int and float
            
                for column_name,coltype in data.dtypes.iteritems():
                    if coltype=='object':
                        list_of_object_columns.append(column_name)
                        categorical_data=list_of_object_columns
                       
                    elif coltype=='float64' or coltype=='int64':
                        list_of_numerical_values_columns.append(column_name)
                        numerical_data=list_of_numerical_values_columns  
                        
                # Hide this warning
                st.set_option('deprecation.showPyplotGlobalUse', False)
            
                #data_slice = data[[scatter_x, scatter_y]]   
                #st.data(data_slice)
                
                #st.write(sns.scatterplot(x=scatter_x, y=scatter_y, data = df))
                #st.pyplot()
            
                 
                scatter_x = st.selectbox("Select a column for X Axis", numerical_data)
                scatter_y = st.selectbox("Select a column for Y Axis", numerical_data)
                
                st.subheader("Scatter Plot")
                st.write(sns.scatterplot(x=scatter_x, y=scatter_y, data = data))
                st.pyplot()  
                #st.title('Scatterplot between carat and price')
                
                #fig = plt.figure()
                #sns.scatterplot(x = data[ scatter_x],y = data[scatter_y])
                #st.pyplot(fig)
                
                
            elif type_of_plot=="continuous data(Heatmap)":
                st.subheader('Correlation: Heatmap')
                
                # or
                #st.write(sns.heatmap(data.corr(), annot=True, linewidths=.5, annot_kws={"size": 7}))
                
                # or
                #mask=np.triu(np.ones_like(data.corr()))
                #st.write(sns.heatmap(data.corr(), annot=True, linewidths=.5, annot_kws={"size": 7}, mask=mask))
                #st.pyplot()    
                
                # or
                fig = plt.figure(figsize = (10,5))
                st.write(sns.heatmap(data.corr(),annot = True , cmap = 'coolwarm' ));
                st.pyplot(fig)
                
            
            elif type_of_plot=="continuous data(Histogram)":
                
                # Create a list of columns objects
                list_of_object_columns=[]
                list_of_numerical_values_columns=[] # int and float
            
                for column_name,coltype in data.dtypes.iteritems():
                    if coltype=='object':
                        list_of_object_columns.append(column_name)
                        categorical_data=list_of_object_columns
                       
                    elif coltype=='float64' or coltype=='int64':
                        list_of_numerical_values_columns.append(column_name)
                        numerical_data=list_of_numerical_values_columns 
                
                st.subheader("Histogram")
               
                #fig = plt.figure()
                
                ax =st.selectbox("Select a numerical item: ", numerical_data)
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.write(sns.displot(data[ax],kde=False))
                st.write(plt.axvline(x=np.mean(data[ax]), color='red', label='mean'))
                st.write(plt.axvline(x=np.median(data[ax]), color='orange', label='median'))
                st.write(plt.legend(loc='upper right'))
                st.pyplot()
                
                

    elif uploaded_file is not None and choice == " Plotting and visualization":
        st.subheader(choice)
        data = pd.read_csv(uploaded_file)
        df = data.copy()
        all_columns = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot", ["bar", "pie", "scatter"]) 

        if type_of_plot=="bar":
            select_columns_to_plot = st.multiselect("Select columns to plot", all_columns)
            cust_data = df[select_columns_to_plot]
            #st.bar_chart(cust_data)
            st.write(sns.catplot(x=all_columns,data=df,kind="count", aspect=1.5))

        elif type_of_plot=="pie":
            select_columns_to_plot = st.selectbox("Select a column", all_columns)
            st.write(df[select_columns_to_plot].value_counts().plot.pie())
            st.pyplot()

        elif type_of_plot=="scatter":
            st.write("Scatter Plot")
            scatter_x = st.selectbox("Select a column for X Axis", all_columns)
            scatter_y = st.selectbox("Select a column for Y Axis", all_columns)
            st.write(sns.scatterplot(x=scatter_x, y=scatter_y, data = df))
            st.pyplot()
             
    #elif uploaded_file is not None and choice == "Our Team": 
    elif choice == "Our Team": 
        st.title("Our Team 🏅")
        st.write("We are students at the University of Massachusetts at Boston and this our team:")
        
        st.balloons()
      
    
        st.subheader("Hey, I am Eduardo :star:")
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/eduardo-s%C3%A1-73b76286/)
        
               ''')
         
        st.subheader("Hi, I am Rich :star:")
        st.markdown('''
             Hi my name is Rich and I am a Senior here at UMASS Boston. I am originally from the Boston area. If you are interested in building more Computer Apps like this one, please contact us. Please feel free to contact me via email: richard.tankle001@umb.edu  \n
        
             Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/richard-tankle-79692b118)
          
               ''')
        
        st.subheader("Hello there! I am Andrice Jules! :star:")
        st.markdown('''
               I am an IT student from Everett, with an aptitude for learning technology. I am expected to Graduate in May 2022 with a Bachelors in Information Technology focusing on System Administrator. Please feel free to contact me via email: andrice.jules001@umb.edu \n

              You can check my LinkedIn Profile:
              - [LinkedIn:](https://www.linkedin.com/in/andricejules)
               ''')
        
        st.subheader("What's up? I am Cai :star:")
        st.markdown('''
              I am an IT student from China. I am expected to Graduate in August 2022 with System Administrator in IT major.Please feel free to contact me via email: guangyao.cai001@umb.edu\n

              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/guangyao-cai-684038233/)
               ''')        

        st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width:350px
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
            width:350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
        )
       

# The Python is executed directly by the python interpreter            
if __name__ == "__main__":
   main() 


        #col1,mid,col2 =st.columns([1,1,20])
        #with col1:
        #    st.image('team_black.png',use_column_width=False)
        #with col2:
        #    st.write("Eduardo")
    
        # Another way
        #image = Image.open('team_black.png')
        #size = (800, 800)
        #image.thumbnail(size)
        #fig = plt.figure()
        #plt.imshow(image)
        #plt.axis("off")
        #st.pyplot(fig)
        
        
        # How to build a Streamlit component - Part 1: Setup and Architecture
        # https://www.youtube.com/watch?v=BuD3gILJW-Q
      
        # FIFA APP
        # https://analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/
        # https://www.kaggle.com/juniorbueno/fifa-2009
        
        # BMI Calculator web app. - Nice to see using if statments 
        # https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/
        
        # Image, video,
        # https://docs.streamlit.io/library/api-reference/media/st.image
        # https://pythonwife.com/layout-streamlit-application/
        
        # pandas for Data Science: Part 2 this is about diamonds
        # https://medium.com/data-science-365/pandas-for-data-science-part-2-c12c3ee876c2