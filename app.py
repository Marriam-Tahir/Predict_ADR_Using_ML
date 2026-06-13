# =========================================================
# IMPORT REQUIRED LIBRARIES
# =========================================================

# Streamlit library for frontend web UI
import streamlit as st

# Joblib library to load encoders
import joblib

# OS library to work with file paths
import os

# Keras library to load deep learning model
import keras

# NumPy library for numerical arrays
import numpy as np


# =========================================================
# PAGE CONFIGURATION
# =========================================================

# Configure Streamlit page settings
st.set_page_config(
    page_title="Clinical ADR Prediction System",   # Browser tab title
    page_icon="💊",                                # Browser tab icon
    layout="wide",                                 # Wide page layout
    initial_sidebar_state="expanded"               # Sidebar opened by default
)

# =========================================================
# ENHANCED PREMIUM MEDICAL / HEALTHCARE UI CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
   PREMIUM MEDICAL AI THEME
   Elegant • Trustworthy • Modern • Soft Clinical UI
========================================================= */


/* =========================================================
   GOOGLE FONT
========================================================= */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');


/* =========================================================
   ROOT COLOR PALETTE
========================================================= */
:root{

    /* Primary */
    --primary: #0f766e;
    --primary-light: #14b8a6;
    --primary-dark: #115e59;

    /* Accent */
    --accent: #2563eb;
    --accent-soft: #60a5fa;

    /* Backgrounds */
    --bg-main: #f4f9fc;
    --bg-card: rgba(255,255,255,0.78);
    --bg-sidebar: linear-gradient(
        180deg,
        #f8fafc 0%,
        #eefaf8 50%,
        #e0f2fe 100%
    );

    /* Text */
    --text-main: #0f172a;
    --text-soft: #475569;

    /* Borders */
    --border: #dbeafe;

    /* Shadow */
    --shadow: 0 10px 35px rgba(15, 23, 42, 0.06);
}


/* =========================================================
   MAIN APP
========================================================= */
.stApp{
    background:
        radial-gradient(circle at top left, #ecfeff 0%, transparent 25%),
        radial-gradient(circle at bottom right, #dbeafe 0%, transparent 30%),
        linear-gradient(135deg, #f8fafc, #f0fdfa, #eff6ff);

    font-family: 'Inter', sans-serif;
    color: var(--text-main);
}


/* =========================================================
   REMOVE DEFAULT PADDING
========================================================= */
.block-container{
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}


/* =========================================================
   PREMIUM GLASS CARD
========================================================= */
.custom-card{
    background: var(--bg-card);
    backdrop-filter: blur(14px);

    border: 1px solid rgba(255,255,255,0.5);
    border-radius: 28px;

    padding: 32px;
    margin-bottom: 25px;

    box-shadow: var(--shadow);
}


/* =========================================================
   MAIN TITLE
========================================================= */
.main-title{
    font-size: 48px;
    font-weight: 800;

    background: linear-gradient(
        135deg,
        #0f766e,
        #2563eb
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-align: center;
    letter-spacing: -1px;

    margin-bottom: 10px;
}

/* =========================================================
   ADD THIS BELOW MAIN TITLE
========================================================= */
.title-container{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    margin-bottom: 12px;
}

.capsule-icon{

    width: 44px;
    height: 44px;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #2563eb 0%,
            #2563eb 50%,
            #ef4444 50%,
            #ef4444 100%
        ) !important;

    transform: rotate(-35deg);

    position: relative;

    box-shadow:
        0 10px 24px rgba(37,99,235,0.25);
}

.capsule-icon::after{

    content: "";

    position: absolute;

    left: 50%;
    top: 0;

    width: 2px;
    height: 100%;

    background: rgba(255,255,255,0.9);

    transform: translateX(-50%);
}


/* =========================================================
   SUBTITLE
========================================================= */
.sub-title{
    font-size: 18px;
    font-weight: 400;
    text-align: center;

    color: var(--text-soft);

    margin-bottom: 35px;
}


/* =========================================================
   SIDEBAR
========================================================= */
section[data-testid="stSidebar"]{

    background: var(--bg-sidebar) !important;

    border-right: 1px solid rgba(255,255,255,0.6) !important;

    box-shadow:
        4px 0 30px rgba(15, 23, 42, 0.05);

    backdrop-filter: blur(18px);
}


/* =========================================================
   SIDEBAR TEXT
========================================================= */
section[data-testid="stSidebar"] *{
    color: var(--text-main) !important;
}


/* =========================================================
   SIDEBAR TITLE
========================================================= */
.sidebar-title{
    font-size: 28px;
    font-weight: 800;

    background: linear-gradient(
        135deg,
        #0f766e,
        #2563eb
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-align: center;

    margin-bottom: 25px;
}


/* =========================================================
   LABELS
========================================================= */
label{
    color: #334155 !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}


/* =========================================================
   INPUTS
========================================================= */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"]{

    background: rgba(255,255,255,0.88) !important;

    border: 1.5px solid #dbeafe !important;

    border-radius: 16px !important;

    color: var(--text-main) !important;

    transition: all 0.25s ease;

    box-shadow:
        inset 0 1px 2px rgba(255,255,255,0.5);
}


/* =========================================================
   INPUT FOCUS
========================================================= */
.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus,
.stSelectbox div[data-baseweb="select"]:focus-within{

    border-color: var(--primary-light) !important;

    box-shadow:
        0 0 0 4px rgba(20,184,166,0.12) !important;
}


/* =========================================================
   PREMIUM BUTTON
========================================================= */
.stButton > button{

    width: 100%;
    height: 60px;

    border: none;
    border-radius: 18px;

    background: linear-gradient(
        135deg,
        #0f766e,
        #2563eb
    );

    color: white !important;

    font-size: 19px;
    font-weight: 700;

    transition: all 0.3s ease;

    box-shadow:
        0 12px 28px rgba(37,99,235,0.22);
}


/* =========================================================
   BUTTON HOVER
========================================================= */
.stButton > button:hover{

    transform: translateY(-3px);

    background: linear-gradient(
        135deg,
        #115e59,
        #1d4ed8
    );

    box-shadow:
        0 18px 36px rgba(37,99,235,0.28);
}


/* =========================================================
   METRIC / INFO CARDS
========================================================= */
[data-testid="stMetric"]{

    background: rgba(255,255,255,0.75);

    border-radius: 20px;

    padding: 18px;

    border: 1px solid rgba(255,255,255,0.7);

    box-shadow: 0 8px 24px rgba(15,23,42,0.05);
}


/* =========================================================
   ALERTS
========================================================= */
.stSuccess,
.stInfo,
.stWarning,
.stError{

    border-radius: 18px !important;

    padding: 18px !important;

    border: none !important;

    box-shadow:
        0 6px 20px rgba(15,23,42,0.04);
}

.stSuccess{
    background: #ecfdf5 !important;
    color: #065f46 !important;
    border-left: 5px solid #10b981 !important;
}

.stInfo{
    background: #eff6ff !important;
    color: #1e40af !important;
    border-left: 5px solid #3b82f6 !important;
}

.stWarning{
    background: #fffbeb !important;
    color: #92400e !important;
    border-left: 5px solid #f59e0b !important;
}

.stError{
    background: #fef2f2 !important;
    color: #991b1b !important;
    border-left: 5px solid #ef4444 !important;
}


/* =========================================================
   EXPANDER
========================================================= */
.streamlit-expanderHeader{

    font-size: 16px;
    font-weight: 600;

    color: #334155;

    background: rgba(255,255,255,0.55);

    border-radius: 12px;

    padding: 8px 12px;
}


/* =========================================================
   TABLES / DATAFRAMES
========================================================= */
[data-testid="stDataFrame"]{

    border-radius: 20px;

    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.6);

    box-shadow:
        0 8px 24px rgba(15,23,42,0.05);
}


/* =========================================================
   HORIZONTAL LINE
========================================================= */
hr{

    border: none;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #cbd5e1,
            transparent
        );

    margin-top: 32px;
    margin-bottom: 32px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# AUTOMATIC DIRECTORY DETECTION
# =========================================================

# Detect current folder automatically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================================================
# LOAD ALL ML ASSETS
# =========================================================

# Cache all files for faster loading
@st.cache_resource
def load_all_ml_assets():

    """
    This function loads:
    1. All label encoders (excluding drug_count_category)
    2. Deep learning Keras model
    """

    # Dictionary containing encoder file names (drug_count_category removed)
    files_to_load = {
        'suspect_drug': 'suspect_drug_encoder.joblib',
        'brand_name': 'brand_encoder.joblib',
        'drug_indication': 'drug_indication_encoder.joblib',
        'pharm_class': 'pharm_class_encoder.joblib',
        'age_group': 'age_group_encoder.joblib',
        'patient_sex': 'patient_sex_encoder.joblib'
    }

    try:

        # Create empty dictionary
        loaded_assets = {}

        # =====================================================
        # LOAD ALL ENCODERS
        # =====================================================
        for key, file_name in files_to_load.items():

            # Create full file path
            full_path = os.path.join(BASE_DIR, file_name)

            # Check if file exists
            if not os.path.exists(full_path):
                return None, None, f"Missing File: '{file_name}' is not in the folder!"

            # Load encoder
            loaded_assets[key] = joblib.load(full_path)

        # =====================================================
        # LOAD KERAS MODEL
        # =====================================================

        # Create model path
        model_path = os.path.join(BASE_DIR, 'model.keras')

        # Check model file
        if not os.path.exists(model_path):
            return None, None, "Missing File: 'model.keras' is not in the folder!"

        # Load deep learning model
        nn_model = keras.models.load_model(model_path)

        # Return loaded files
        return loaded_assets, nn_model, "Success"

    except Exception as e:

        # Return loading error
        return None, None, f"Loading Error: {str(e)}"


# =========================================================
# INITIALIZE ASSETS
# =========================================================

# Load assets
assets, model, status = load_all_ml_assets()


# =========================================================
# VERIFY FILES LOADED
# =========================================================

if status != "Success":

    # Show error if files missing
    st.error(f"❌ Asset Loading Error: {status}")

    # Show helper message
    st.info("Make sure all encoder files and model.keras exist in the same folder.")
    

else:
    
    # =====================================================
    # MAIN TITLE SECTION
    # ===================================================== 
    st.markdown("""
   <div class="title-container">
   <div class="capsule-icon"></div>

    <div class="main-title">
        Clinical Adverse Drug Reaction Prediction System
    </div>
    </div>
""", unsafe_allow_html=True)

    st.markdown(
        '<div class="sub-title">AI-Powered Deep Learning Diagnostics for Automated Patient Safety Risk Analysis</div>',
        unsafe_allow_html=True
    )

    # # Create card container
    # st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    # Instructions heading
    st.subheader("📌 System Instructions")

    # Instructions message
    st.info(
        "Use the features panel on the left sidebar to enter comprehensive patient details and therapeutic profiles. "
        "Verify all configurations before executing data pipeline evaluations."
    )
    
    # Close card
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # SIDEBAR SECTION
    # =====================================================

    # Sidebar title
    st.sidebar.markdown('<div class="sidebar-title">📋 Input Features Panel</div>', unsafe_allow_html=True)

    # Divider line
    st.sidebar.markdown("---")

    # =====================================================
    # SEARCHABLE FIELDS
    # =====================================================

    st.sidebar.subheader("🔬 Drug & Clinical Information")

    # Suspect drug dropdown
    suspect_list = ["-- Type to Search Suspect Drug --"] + list(
        assets['suspect_drug'].classes_
    )

    selected_suspect = st.sidebar.selectbox(
        "Suspect Drug",
        options=suspect_list
    )

    # Brand name dropdown
    brand_list = ["-- Type to Search Brand --"] + list(
        assets['brand_name'].classes_
    )

    selected_brand = st.sidebar.selectbox(
        "Brand Name",
        options=brand_list
    )

    # Drug indication dropdown
    ind_list = ["-- Type to Search Indication --"] + list(
        assets['drug_indication'].classes_
    )

    selected_ind = st.sidebar.selectbox(
        "Drug Indication (Condition)",
        options=ind_list
    )

    # Pharmacological class dropdown
    class_list = ["-- Type to Search Class --"] + list(
        assets['pharm_class'].classes_
    )

    selected_class = st.sidebar.selectbox(
        "Pharmacological Class",
        options=class_list
    )

    # Divider line
    st.sidebar.markdown("---")

    # =====================================================
    # PATIENT PROFILE SECTION (drug_count_category completely removed)
    # =====================================================

    st.sidebar.subheader("👤 Patient & Metric Profiles")

    # Numerical input for total drugs
    num_drugs = st.sidebar.number_input(
        "Total Number of Drugs (num_drugs)",
        min_value=1,
        max_value=100,
        value=1
    )

    # Age group dropdown
    age_group_list = list(assets['age_group'].classes_)

    selected_age_group = st.sidebar.selectbox(
        "Patient Age Group",
        options=age_group_list
    )

    # Sex dropdown
    sex_options = ["Male", "Female", "Other"]

    selected_sex_label = st.sidebar.selectbox(
        "Patient Sex",
        options=sex_options
    )

    # =====================================================
    # VALIDATION CHECKS
    # =====================================================

    placeholder_checks = [
        selected_suspect == "-- Type to Search Suspect Drug --",
        selected_brand == "-- Type to Search Brand --",
        selected_ind == "-- Type to Search Indication --",
        selected_class == "-- Type to Search Class --"
    ]

    # =====================================================
    # MAIN PREDICTION SECTION
    # =====================================================

    st.markdown("## 📊 Process Analysis")

    # Prediction button
    if st.button("🚀 Predict Adverse Reaction"):

        # Check empty fields
        if any(placeholder_checks):

            st.warning(
                "⚠️ Action Required: Enter Input   before initiating inference calculations."
            )

        else:

            # Loading spinner
            with st.spinner("Processing architectural tensors & assessing clinical vulnerabilities..."):

                try:

                    # =================================================
                    # TRANSFORM INPUTS USING ENCODERS
                    # =================================================

                    id_suspect = assets['suspect_drug'].transform(
                        [selected_suspect]
                    )[0]

                    id_brand = assets['brand_name'].transform(
                        [selected_brand]
                    )[0]

                    id_ind = assets['drug_indication'].transform(
                        [selected_ind]
                    )[0]

                    id_class = assets['pharm_class'].transform(
                        [selected_class]
                    )[0]

                    id_age = assets['age_group'].transform(
                        [selected_age_group]
                    )[0]

                    # =================================================
                    # MANUAL SEX MAPPING
                    # =================================================

                    sex_mapping = {
                        "Male": 1,
                        "Female": 2,
                        "Other": 0
                    }

                    id_sex = sex_mapping[selected_sex_label]

                    # =================================================
                    # CREATE FEATURE VECTOR (Cleaned 7-Column Layout)
                    # =================================================

                    raw_vector = [[
                        id_suspect,
                        id_brand,
                        id_ind,
                        id_class,
                        num_drugs,
                        id_age,
                        id_sex
                    ]]

                    # Convert into NumPy array
                    feature_vector = np.array(
                        raw_vector,
                        dtype=np.int32
                    )
                     # =================================================
                    # MODEL PREDICTION (FIXED SECTION)
                    # =================================================

                    raw_prediction = model.predict(feature_vector)

                    risk_score = float(raw_prediction[0][0])
                    risk_score = max(0.0, min(risk_score, 1.0)) * 100

                    st.markdown("---")
                    st.header("📈 Evaluation Results")
                    if risk_score >= 85:
                        st.error(f"🚨 CRITICAL HIGH RISK: {risk_score:.2f}% (Serious Adverse Event Likely)")
                        
                        st.markdown("### 📋 Clinical Recommendations & Action Plan")
                        st.markdown("""
                        1. **Act Quickly:** Inform the doctor or pharmacist immediately because the patient may have a serious drug reaction.

2. **Review the Medicine:** Consider stopping or changing the suspected medicine (**{0}**) if a safer option is available.

3. **Monitor the Patient:** Regularly check vital signs and perform necessary kidney, liver, or blood tests.

4. **Update Records:** Record this case in the patient’s electronic health record (EHR) as a possible serious drug risk.

                        """.format(selected_suspect))

                    elif risk_score >= 60:
                        st.warning(f"⚠️ MODERATE-HIGH RISK: {risk_score:.2f}% (Elevated Sensitivity Profile)")
                        
                        st.markdown("### 📋 Clinical Recommendations & Action Plan")
                        st.markdown("""
                        **1.Careful Monitoring:** Inform the medical team to watch for early side effects from {0}.
**2.Check Dosage:** Review whether the medicine dose should be adjusted based on age, kidney, or liver condition.
**3.Review All Medicines:** The patient is taking {1} medicine(s), so check for possible harmful drug interactions.
**4.Guide the Patient:** Tell the patient or caregiver to report any unusual symptoms immediately.
                        """.format(selected_suspect, num_drugs))

                    elif risk_score >= 35:
                        st.info(f"🟡 MODERATE RISK: {risk_score:.2f}% (Mild to Borderline Clinical Profile)")
                        
                        st.markdown("### 📋 Clinical Recommendations & Action Plan")
                        st.markdown("""
                        1. **Regular Monitoring:** Continue the normal treatment for **{0}** and schedule a follow-up check within 48–72 hours.

2. **Check Patient Condition:** Make sure the patient’s kidney, liver, and overall health condition are suitable for this medicine.

3. **Track Symptoms:** Give the patient a simple checklist to monitor and report any side effects.

                        """.format(selected_suspect))

                    else:
                        st.success(f"✅ LOW RISK PROFILE: {risk_score:.2f}% (Cleared Patient Configuration)")
                        
                        st.markdown("### 📋 Clinical Recommendations & Action Plan")
                        st.markdown("""
                        1. **Continue Current Treatment:** No major risk has been detected by the AI system. Continue the medicine as prescribed.

2. **Regular Care:** Follow normal hospital guidelines and routine patient monitoring procedures.

3. **Recheck if Needed:** Repeat this assessment if new medicines are added or the patient’s health condition changes.

                        """)

                except Exception as e:
                    st.error(f"Execution Error: {e}")

