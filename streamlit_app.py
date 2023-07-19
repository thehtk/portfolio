import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Hitesh Kumar
##### *Resume* 
''')



image = Image.open('dp3.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/thehtk/" target="_blank">Hitesh Kumar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')





txt('**Bachelor of Engineering** CSE (Hons.), *Chandigarh University*, Punjab',
'Aug 2020 - Jun 2024')
st.markdown('''
- Specialization in AIML in association with IBM
''')



txt('**Senior Secondary (XII)** Non-Medical, *Delhi Public School*, Jabalpur',
'Apr 2019 - Apr 2020')
st.markdown('''
- Completed classes XI and XII. 
- Scored 94% in Computer Science in class XII.
''')



#####################
st.markdown('''
## Work Experience
''')




txt('**Website Developer**, Saralsoft LLC',
'Aug 2022')
st.markdown('''
- Spearheaded website development initiatives, providing innovative solutions to enhance user experience and increase traffic.
- Utilized cutting-edge technologies and programming languages to create robust and responsive websites that were optimized for search engines and mobile devices.
- Demonstrated a strong commitment to customer satisfaction, ensuring prompt and effective resolution of all website-related inquiries and concerns.
''')

txt('**Business Analyst**, Saralsoft LLC',
'Jun 2022 - Jul 2022')
st.markdown('''
- Strategically analyze and determine the most effective methods to communicate a company's products and vision
- Conduct informative and engaging sessions to increase student awareness and knowledge of a company's operations and culture
- Effectively communicate complex technical concepts to non-technical stakeholders in a clear and concise manner
''')




#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C/C++`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/thehtk/')
txt2('GitHub', 'https://github.com/thehtk')
