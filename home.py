import streamlit as st


# Custom CSS for an elegant, modern card layout
st.markdown("""
    <style>
        body {
            background-color: #f4f8fb;
        }
        .main-title {
            color: #1565c0;
            font-size: 2.7em;
            font-weight: 900;
            text-align: center;
            margin-bottom: 0.2em;
            letter-spacing: 0.03em;
        }
        .subtitle {
            color: #1976d2;
            font-size: 1.15em;
            text-align: center;
            margin-bottom: 2em;
        }
        .card-outer {
            display: flex;
            flex-direction: column;
            height: 100%;
            justify-content: space-between;
        }
        .card-inner {
            background: linear-gradient(135deg, #e3f0fa 0%, #fff 100%);
            border-radius: 18px;
            box-shadow: 0 6px 32px 0 rgba(21,101,192,0.07);
            padding: 1.6em 1.4em 1.3em 1.4em;
            min-height: 340px;
            margin-bottom: 1em;
            border-left: 7px solid #1565c0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: box-shadow 0.2s;
        }
        .card-inner:hover {
            box-shadow: 0 10px 36px 0 rgba(21,101,192,0.13);
        }
        .blue-subheader {
            color: #1565c0;
            font-size: 1.22em;
            font-weight: 800;
            margin-bottom: 0.6em;
            letter-spacing: 0.02em;
        }
        .card-content {
            font-size: 1.01em;
            color: #263238;
            margin-bottom: 1.1em;
        }
        .vertical-divider {
            border-left: 2.5px solid #bbdefb;
            height: 340px;
            margin: 0 auto;
        }
        .st-emotion-cache-7ym5gk {
            background-color: #f4f8fb;
        }
        .appendix {
            background-color: #e3f0fa;
            border-radius: 12px;
            padding: 1.2em 1em 1em 1.2em;
            margin-top: 2.2em;
        }
        .appendix-header {
            color: #1565c0;
            font-size: 1.10em;
            font-weight: 700;
            margin-bottom: 0.6em;
        }
        .stPageLink {
            margin-top: 0.4em !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Gen AI Use Case Demo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to the AWS Bedrock use case Demo </div>', unsafe_allow_html=True)
st.markdown("---")

col1, col_div, col2 = st.columns([5, 1, 5])

with col1:
    # st.markdown('<div class="card-outer"><div class="card-inner">', unsafe_allow_html=True)
    st.markdown('<div class="blue-subheader">Plan Audit</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-content">
    <ul>
        <li>Automates extraction of critical information from PDF plan documents.</li>
        <li>Uses a Retrieval-Augmented Generation (RAG) architecture for enhanced document understanding and retrieval.</li>
        <li>Advanced Large Language Models (LLMs) generate dynamic queries for targeted data extraction.</li>
        <li>Efficiently retrieves policy-specific provisions and insights from PDF content.</li>
        <li>The solution improves efficiency, accuracy, and scalability in complex plan document audits.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("plan_audit_page.py", label="🔗 Plan Audit Demo", icon="➡️")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_div:
    st.markdown('<div class="vertical-divider"></div>', unsafe_allow_html=True)

with col2:
    # st.markdown('<div class="card-outer"><div class="card-inner">', unsafe_allow_html=True)
    st.markdown('<div class="blue-subheader">Fixed Income - Quarter Back</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-content">
    <ul>
        <li>Automates classification of emails and documents using advanced LLMs.</li>
        <li>Uses both email and PDF text as context for precise categorization.</li>
        <li>Combines keyword and intent detection for categories and sub-categories.</li>
        <li>Classifies communications into 7 key categories for streamlined processing.</li>
        <li>Enables efficient operations team quarter back and smart routing.</li>
        <li>The solution enhances productivity and reduces manual effort by automating the triage and routing process for incoming emails and documents.</li>
                       
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("fixed_income_page.py", label="🔗 Quarter Back Demo", icon="➡️")
    st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown("---")


st.markdown('</div>', unsafe_allow_html=True)
st.caption("© infosys bpm aws gen ai tool - for demonstration purposes only")