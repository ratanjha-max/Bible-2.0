import streamlit as st

# Page Configuration
st.set_page_config(page_title="Paytm UPHD Bot", page_icon="🔵")

# Title and Header
st.title("🤖 Fintech Merchant Support Bot")
st.markdown("### SOP: Primary Number Change Request")
st.info("Follow each step carefully as per UPHD guidelines.")

# --- STEP 1: PRE-CHECK ---
st.header("Step 1 & 2: Initial Screening")
mid_input = st.text_input("Enter Merchant MID:")
mid_category = st.selectbox("Select MID Type:", ["Select", "Retail", "EDC", "Online", "Corporate", "Enterprise"])

if mid_category in ["EDC", "Online", "Corporate", "Enterprise"]:
    st.error("❌ Process Denied: This MID type is not handled here. Refer to specific team SOP.")
elif mid_category == "Retail":
    boss_check = st.radio("Is this NEW number already present on BOSS Panel?", ["Not Checked", "Yes (MID Found)", "No (MID Not Found)"])
    
    if boss_check == "Yes (MID Found)":
        st.warning("⚠️ Action: Politely deny. New number must not be linked to any existing MID.")
    elif boss_check == "No (MID Not Found)":
        
        # --- STEP 3: OAUTH CHECK ---
        st.header("Step 3: Oauth Verification")
        oauth_status = st.radio("Is the number registered on Oauth?", ["No", "Yes"])
        
        if oauth_status == "No":
            st.info("📢 Action: Ask the merchant to register on Oauth first.")
        else:
            # --- STEP 4: DOCUMENTATION ---
            st.header("Step 4: Documents & Reason")
            reason = st.selectbox("Reason for Change:", ["Select", "Employee Left/Number Closed", "SIM/Phone Lost"])
            entity = st.radio("Entity Type:", ["Proprietorship", "Non-Proprietorship"])
            
            if reason != "Select":
                st.subheader("Checklist of Documents to Collect:")
                
                if reason == "SIM/Phone Lost":
                    st.markdown("- [ ] **MANDATORY: FIR Copy or Police Complaint**")
                
                st.markdown("- [ ] Registration Certificate / COI")
                st.markdown("- [ ] PAN of Business/Proprietor")
                st.markdown("- [ ] Declaration Form on Letterhead (Signed)")

                # --- STEP 5: VALIDATION ---
                st.header("Step 5: Validation")
                docs_ok = st.radio("Are documents satisfactory and matching BOSS details?", ["Pending", "No", "Yes"])
                
                if docs_ok == "No":
                    st.error("Action: Ask for complete/relevant documents.")
                elif docs_ok == "Yes":
                    # --- STEP 6, 7 & 8: EXECUTION ---
                    st.header("Step 6, 7 & 8: Execution & Closure")
                    
                    with st.expander("📧 Step 6: Send P2M Disable Request"):
                        st.write("**Send to:** ratan.jha@paytm.com, sudhanshu.pandey@paytm.com, shwetank1.singh@paytm.com")
                        st.write("**L2/L3:** chetan.singh@paytm.com, nikhil.chandra@paytm.com")
                    
                    st.markdown("### [📝 Step 7: Update Tracker](https://docs.google.com/spreadsheets/d/1oV7XzOVV3uEZ6bsIF3H0_mP4wu2NF8J7WN4wIAvQzKo/edit#gid=0)")
                    st.write("TAT to share: **24-48 Hours**")
                    
                    st.divider()
                    st.subheader("Final Status")
                    final_check = st.radio("Is details updated on BOSS Panel now?", ["Processing", "Yes", "No"])
                    
                    if final_check == "Yes":
                        new_num = st.text_input("Enter Updated Number:")
                        st.success("✅ Case Resolved! Use Macro below:")
                        macro = f"Dear Merchant,\nWarm greetings!\n\nAs requested, your primary number has been updated to {new_num} against the shared MID : {mid_input}.\n\nRegards,\nBusiness Helpdesk Team"
                        st.code(macro)
                    elif final_check == "No":
                        st.warning("Action: Check 'Boss data correction sheet' or contact Chetan Singh.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("v1.0 | Paytm UPHD Support Assistant")