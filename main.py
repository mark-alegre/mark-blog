import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


#1. as sidebar menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("profile-pic3.png")
img_contact_form2 = Image.open("food.png")
img_contact_form3 = Image.open("boracay.png")
img_lottie_animation = Image.open("boracay.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("WELCOME TO THE PHILIPPINES 😉")
    st.title("Also known as Gems of the East. Moreover, named to be Orphans of the Pacific and Land of the Morning.")
    st.write(
        "Let's emerged to the beauty of the Land of the Morning the PHILIPPINES"
    )
    st.write("[Learn More >](https://www.youtube.com/watch?v=nQvoTSHV13A)")

# ---- AUTHOR'S BACKGROUND ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns([1,2])
    
    with right_column:
        st.header("ABOUT THE AUTHOR")
        st.write("##")
        st.write(
            """
            PERSONAL INFORMATION
            - Hi everyone, I am JARELLE ANN MARIZ C. MORENO,
             a college student studying in the SURIGAO DEL NORTE STATE UNIVERSITY.
            
            EDUCATIONAL BACKGROUND
            - Elementary: SABANG ELEMENTARY SCHOOL
            - Junior High School: SISTERS OF MARY SCHOOL-GIRLSTOWN, INC.
            - Senior High School: SISTERS OF MARY SCHOOL-GIRLSTOWN, INC.
            - College Education: SURIGAO DEL NORTE STATE UNIVERSITY
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with left_column:
        st.image(img_contact_form)
        

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form3)
    with text_column:
        st.subheader("TOURIST SPOTS THAT WILL MAKE YOU AWE")
        st.write(
            """
            Tourism plays vital role in the economic development of one country.
            Here in the Philippine setting, there are so many tourist spots and destinations.
            Which in fact made the country famous for and keeps attacts tourist to come over.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=ZjFzkhrqIZs)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("FOODS IN THE PHILIPPINES IS A BIG DRAW")
        st.write(
            """
            Food is very vital in our body. In the Philippines, as culture and tourism is a hit, food is also a big draw.
            Food in here is diverse and unique mixing both Asian and European influences.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=lw3_W5X1t54)")
    with text_column:
        st.write(
            "To find more about the FOODS in this magnificent country, please click the link below"
        )
        st.markdown("https://theplanetd.com/bes-filipino-food/")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()