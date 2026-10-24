"""
RamaBJP Maintenance Work Orders Page
"""

import streamlit as st
import pandas as pd
from repositories.maintenance_repo import (
    get_all_work_orders, create_work_order, get_work_order_by_id,
    update_work_order_status, assign_work_order, delete_work_order,
    get_work_order_stats
)
from repositories.equipment_repo import get_all_equipment
from config.theme import COLORS, get_status_badge


def render_maintenance():
    """Render the maintenance page."""
    st.markdown("## 📋 Maintenance Work Orders")
    st.markdown("Create, assign and track maintenance work orders")
    st.markdown("---")
    
    # ============================================================
    # STATS
    # ============================================================
    stats = get_work_order_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Work Orders", stats["total"])
    with col2:
        st.metric("Open", stats["open"])
    with col3:
        st.metric("In Progress", stats["in_progress"])
    with col4:
        st.metric("Completed", stats["completed"])
    
    st.markdown("---")
    
    # ============================================================
    # TABS
    # ============================================================
    tab1, tab2 = st.tabs(["📋 View All", "➕ Create New"])
    
    # ============================================================
    # TAB 1: VIEW ALL
    # ============================================================
    with tab1:
        work_orders = get_all_work_orders()
        
        if not work_orders:
            st.info("No work orders found.")
            return
        
        for wo in work_orders:
            status = wo["status"]
            priority = wo["priority"]
            
            status_color = {
                "Open": COLORS["info"],
                "In Progress": COLORS["warning"],
                "Completed": COLORS["success"]
            }.get(status, COLORS["unknown"])
            
            priority_color = {
                "Low": COLORS["success"],
                "Medium": COLORS["info"],
                "High": COLORS["warning"],
                "Critical": COLORS["critical"]
            }.get(priority, COLORS["unknown"])
            
            with st.expander(f"{wo['work_order_id']} — {wo.get('equipment_name', wo['equipment_id'])} — {status}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Issue:** {wo['issue']}")
                    st.markdown(f"**Equipment:** {wo['equipment_id']}")
                    st.markdown(f"**Priority:** {priority}")
                    st.markdown(f"**Assigned To:** {wo.get('assigned_to', 'Unassigned')}")
                    st.markdown(f"**Planned Date:** {wo.get('planned_date', 'N/A')}")
                    st.markdown(f"**Created:** {wo['created_at'][:19]}")
                    
                    if wo.get('completed_date'):
                        st.markdown(f"**Completed:** {wo['completed_date'][:19]}")
                    if wo.get('work_performed'):
                        st.markdown(f"**Work Performed:** {wo['work_performed']}")
                    if wo.get('notes'):
                        st.markdown(f"**Notes:** {wo['notes']}")
                
                with col2:
                    st.markdown(f"**Status:** {get_status_badge(status)}", unsafe_allow_html=True)
                    st.markdown(f"**Priority:** {get_status_badge(priority)}", unsafe_allow_html=True)
                    
                    st.markdown("---")
                    
                    if status == "Open":
                        if st.button(f"▶️ Start", key=f"start_{wo['work_order_id']}"):
                            update_work_order_status(wo['work_order_id'], "In Progress")
                            st.success("Started!")
                            st.rerun()
                    
                    if status == "In Progress":
                        work_done = st.text_input("Work performed", key=f"work_{wo['work_order_id']}")
                        if st.button(f"✔️ Complete", key=f"complete_{wo['work_order_id']}"):
                            update_work_order_status(wo['work_order_id'], "Completed", work_done)
                            st.success("Completed!")
                            st.rerun()
                    
                    if st.button(f"🗑️ Delete", key=f"del_{wo['work_order_id']}"):
                        delete_work_order(wo['work_order_id'])
                        st.success("Deleted!")
                        st.rerun()
    
    # ============================================================
    # TAB 2: CREATE NEW
    # ============================================================
    with tab2:
        st.markdown("### Create Work Order")
        
        equipment_list = get_all_equipment()
        if not equipment_list:
            st.warning("No equipment available.")
            return
        
        eq_ids = [e["equipment_id"] for e in equipment_list]
        
        with st.form("create_work_order_form"):
            equipment_id = st.selectbox("Equipment *", eq_ids)
            issue = st.text_area("Issue Description *", placeholder="Describe the issue...")
            
            col1, col2 = st.columns(2)
            with col1:
                priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"], index=1)
            with col2:
                assigned_to = st.text_input("Assign To", placeholder="Technician name")
            
            planned_date = st.date_input("Planned Date")
            notes = st.text_area("Notes", placeholder="Optional notes")
            
            submitted = st.form_submit_button("➕ Create Work Order", use_container_width=True)
            
            if submitted:
                if not issue:
                    st.error("❌ Issue description is required.")
                else:
                    wo_id = create_work_order(
                        equipment_id, issue, priority,
                        assigned_to, str(planned_date), notes
                    )
                    if wo_id:
                        st.success(f"✅ Work Order {wo_id} created!")
                        st.rerun()
                    else:
                        st.error("❌ Failed to create work order.")