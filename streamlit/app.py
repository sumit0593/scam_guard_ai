# streamlit_app/app.py

import sys
from pathlib import Path

# Add the project root directory to Python path using pathlib
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd
from pipeline.scam_detector.detector import ScamDetector

st.set_page_config(page_title="Scam Detection App", layout="wide")
st.title("Scam Detection")

# Detector instance
detector = ScamDetector()

user_input = st.text_area("Enter the message to analyze:", height=150, 
                            placeholder="Example: Congratulations! You've won $1000. Click here to claim...")

if st.button("Analyze Message", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        with st.spinner("Analyzing..."):
            result = detector.detect(user_input)
        
        st.success("Analysis completed!")
        
        # Display results
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Main prediction
            label = result.get("label", "Uncertain")
            if label == "Scam":
                st.error(f"**PREDICTION: {label}**")
            elif label == "Not Scam":
                st.success(f"**PREDICTION: {label}**")
            else:
                st.warning(f"**PREDICTION: {label}**")
            
            # Intent
            intent = result.get("intent", "Unknown")
            st.info(f"**Intent Detected:** {intent}")
        
        with col2:
            # Risk factors
            risk_factors = result.get("risk_factors", [])
            if risk_factors:
                st.subheader("Risk Factors")
                for factor in risk_factors:
                    st.text(f"• {factor}")
        
        # Reasoning (expandable)
        reasoning = result.get("reasoning", "No reasoning provided")
        with st.expander("AI Reasoning Process", expanded=False):
            st.write(reasoning)