"""
ISCFIT Platform Reporting Cockpit - Main Dashboard Application
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))
# if str(project_root) not in sys.path:
#     sys.path.insert(0, str(project_root))

from config.app_config import APPLICATIONS, UI_CONFIG, NAVIGATION_CONFIG, get_apps_by_category
from utils.common import (
    apply_custom_css, display_header, display_category_header, 
    create_app_card, load_app_module, open_external_link, 
    show_about, handle_navigation
)

def initialize_session_state():
    """Initialize session state variables"""
    if 'current_app' not in st.session_state:
        st.session_state.current_app = None
    if 'show_about' not in st.session_state:
        st.session_state.show_about = False
    if 'filter_category' not in st.session_state:
        st.session_state.filter_category = None

def render_home_page():
    """Render the main dashboard home page"""
    # Display main header
    display_header()
    
    # Get applications grouped by category
    categories = get_apps_by_category()
    
    # Filter by category if specified
    if st.session_state.filter_category:
        categories = {k: v for k, v in categories.items() 
                     if k == st.session_state.filter_category}
        if st.button("🔙 Show All Categories", key="show_all"):
            st.session_state.filter_category = None
            st.rerun()
    
    # Render each category
    for category, apps in categories.items():
        display_category_header(category)
        
        # Create columns for cards (2 per row as configured)
        cols_per_row = NAVIGATION_CONFIG["cards_per_row"]
        
        # Split apps into rows
        for i in range(0, len(apps), cols_per_row):
            cols = st.columns(cols_per_row)
            row_apps = apps[i:i + cols_per_row]
            
            for j, (app_id, config) in enumerate(row_apps):
                if create_app_card(app_id, config, cols[j]):
                    handle_app_selection(app_id, config)

def handle_app_selection(app_id: str, config):
    """Handle application selection and navigation"""
    if config.app_type == "streamlit":
        # Navigate to Streamlit app
        st.session_state.current_app = app_id
        st.rerun()
    elif config.app_type == "powerapps":
        # Open PowerApps tool
        if config.url:
            open_external_link(config.url, config.name)
        else:
            st.error(f"No URL configured for {config.name}")

def render_streamlit_app(app_id: str):
    """Render a Streamlit application with professional styling"""
    config = APPLICATIONS[app_id]
    
    # Load and run the app module
    module = load_app_module(config.module)
    if module and hasattr(module, 'main'):
        try:
            # Display professional app header with consistent styling - reduced size for Monthly OPL Report
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 15px;
                margin: 0.5rem 0 1.5rem 0;
                text-align: center;
                box-shadow: 0 6px 20px rgba(46, 134, 171, 0.3);
                position: relative;
                overflow: hidden;
            ">
                <div style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
                    pointer-events: none;
                "></div>
                <div style="position: relative; z-index: 1;">
                    <div style="font-size: 1.8rem; margin-bottom: 0.3rem;">{config.icon}</div>
                    <h1 style="
                        font-family: 'Inter', sans-serif;
                        font-size: 1.8rem;
                        font-weight: 700;
                        margin: 0.3rem 0;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                        letter-spacing: 1px;
                        text-transform: uppercase;
                    ">{config.name}</h1>
                    <p style="
                        font-family: 'Inter', sans-serif;
                        font-size: 0.85rem;
                        font-weight: 400;
                        margin: 0.3rem 0;
                        opacity: 0.95;
                        line-height: 1.5;
                        letter-spacing: 1px;
                    ">{config.description}</p>
                    <div style="
                        margin-top: 0.3rem;
                        padding: 0.3rem 0.8rem;
                        background: rgba(255, 255, 255, 0.2);
                        border-radius: 20px;
                        display: inline-block;
                        font-size: 0.7rem;
                        font-weight: 500;
                    ">
                        📊 Interactive Analytics Dashboard
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Run the app
            module.main()
        except Exception as e:
            st.error(f"Error running {config.name}: {str(e)}")
            st.info("Please check the application code and try again.")
    else:
        st.error(f"Could not load application: {config.name}")
        st.info(f"Make sure the module '{config.module}' exists and has a 'main()' function.")

def main():
    """Main application entry point"""
    # Configure page
    st.set_page_config(
        page_title=UI_CONFIG["page_title"],
        page_icon="📊",
        layout=UI_CONFIG["layout"],
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Apply custom CSS
    apply_custom_css()
    
    # Handle sidebar navigation - skip for OPL report, Daily Incident report, and License Tracker as they have their own navigation
    if not (st.session_state.current_app in ["monthly_opl", "daily_incident", "licensing"]):
        handle_navigation()
    
    # Main content area
    if st.session_state.show_about:
        show_about()
    elif st.session_state.current_app:
        # Render specific app
        render_streamlit_app(st.session_state.current_app)
    else:
        # Render home page
        render_home_page()

if __name__ == "__main__":

    main()
