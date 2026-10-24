"""
RamaBJP Research & Problem Challenge Page
"""

import streamlit as st
from config.theme import COLORS


def render_research():
    """Render the research page."""
    st.markdown("## 📚 Research & Problem Challenge")
    st.markdown("Understanding predictive maintenance and the problem we solve")
    st.markdown("---")
    
    # ============================================================
    # WHAT IS PREDICTIVE MAINTENANCE
    # ============================================================
    st.markdown("### What is Predictive Maintenance?")
    st.markdown("""
    Predictive maintenance uses **condition data** (vibration, temperature, oil quality) 
    to predict when equipment might fail, so maintenance can be planned **before** a breakdown occurs.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("""
        **🔧 REACTIVE**
        
        Fix after failure
        
        - ❌ Unplanned downtime
        - ❌ High cost
        - ❌ No warning
        """)
    
    with col2:
        st.warning("""
        **📅 PREVENTIVE**
        
        Fix on fixed schedule
        
        - ⚠️ Some downtime
        - ⚠️ Medium cost
        - ⚠️ May be unnecessary
        """)
    
    with col3:
        st.success("""
        **🎯 PREDICTIVE**
        
        Fix before failure
        
        - ✅ Planned downtime
        - ✅ Lower cost
        - ✅ Early warning
        """)
    
    st.markdown("---")
    
    # ============================================================
    # WHY IT MATTERS
    # ============================================================
    st.markdown("### Why It Matters in Defence MRO")
    st.markdown("""
    Defence equipment operates in demanding conditions. Unexpected failures can:
    - **Delay missions** — Equipment not ready when needed
    - **Increase repair costs** — Emergency repairs cost more
    - **Reduce operational readiness** — Less equipment available
    - **Risk personnel safety** — Equipment failure during operation
    """)
    
    st.markdown("---")
    
    # ============================================================
    # WHY RULES NOT AI
    # ============================================================
    st.markdown("### Why This Prototype Uses Rules, Not AI")
    
    st.markdown("""
    | Rule-Based Logic | AI/ML Model |
    | :--- | :--- |
    | ✅ Transparent — anyone can see why alert appears | ❌ Black box — hard to explain |
    | ✅ No training dataset needed | ❌ Needs large historical data |
    | ✅ Deterministic — same input, same output | ❌ Probabilistic — may vary |
    | ✅ Easy to update thresholds | ❌ Requires retraining |
    """)
    
    st.markdown("---")
    
    # ============================================================
    # LIMITATIONS
    # ============================================================
    st.markdown("### Current Limitations")
    
    st.warning("""
    - This is a **Proof of Concept** — not a deployed system
    - Uses **synthetic demo data** — not real equipment readings
    - **Rule-based logic** — not AI/ML
    - **No live sensor connection** — data is simulated
    - **Thresholds are illustrative** — not official specifications
    - **Failure prediction is NOT validated**
    """)