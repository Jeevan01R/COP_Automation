# ISCFIT Platform Reporting Cockpit

A comprehensive Streamlit-based dashboard application that provides centralized access to reporting tools and applications for the ISCFIT platform.

## Features

### 🎯 **Main Dashboard**
- **Welcome Screen**: Professional landing page with easy navigation
- **Modular Design**: Individual applications are self-contained and easily integrated
- **Responsive Layout**: Works on desktop and mobile devices
- **Beautiful UI**: Modern design with gradients and professional styling

### 📊 **Streamlit Applications**
1. **Daily Incident Outlier Report** - Analyze daily incident patterns and detect outliers
2. **Weekly Open Feature Report** - Track weekly feature development progress
3. **Monthly OPL Report** - Comprehensive operational performance learning reports
4. **Utilization Report** - Resource utilization analysis and optimization

### 🔗 **PowerApps Integration**
- **Semaphore PowerApps Tool** - Direct links to external PowerApps tools
- **TH Handbook PowerApps Tool** - Technical handbook access
- **DataUpload PowerApps Tool** - Data upload and management

## Project Structure

```
iscfit_platform/
├── main.py                    # Main dashboard application
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── config/
│   ├── __init__.py
│   └── app_config.py         # Application configuration and registry
├── utils/
│   ├── __init__.py
│   └── common.py             # Common utilities and styling
├── apps/
│   ├── __init__.py
│   ├── daily_incident_report.py      # Daily incident analysis
│   ├── weekly_feature_report.py      # Weekly feature tracking
│   ├── monthly_opl_report.py         # Monthly OPL reports
│   └── utilization_report.py         # Resource utilization
└── assets/                   # Static assets (images, etc.)
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd iscfit_platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Access the dashboard**
   - Open your browser and go to `http://localhost:8501`
   - The main dashboard will load with all available applications

## Usage

### Navigation
- **Home Button**: Return to the main dashboard
- **About Button**: View application information
- **Sidebar Filters**: Use category filters for quick access

### Adding New Applications

#### For Streamlit Applications:

1. **Create a new Python file** in the `apps/` directory:
   ```python
   # apps/my_new_report.py
   import streamlit as st
   
   def main():
       st.title("My New Report")
       st.write("Your application content here...")
       
   if __name__ == "__main__":
       main()
   ```

2. **Register the application** in `config/app_config.py`:
   ```python
   "my_new_report": AppConfig(
       name="My New Report",
       description="Description of your new report",
       module="apps.my_new_report",
       icon="📈",
       app_type="streamlit",
       category="Custom Reports"
   )
   ```

#### For PowerApps Tools:

Add to the `APPLICATIONS` dictionary in `config/app_config.py`:
```python
"my_powerapps_tool": AppConfig(
    name="My PowerApps Tool",
    description="Description of your PowerApps tool",
    module="",
    icon="🔧",
    app_type="powerapps",
    url="https://your-powerapps-url.com",
    category="External Tools"
)
```

### Customization

#### Styling
- Modify `utils/common.py` to customize the CSS styling
- Update color schemes in the `apply_custom_css()` function

#### Configuration
- Update `config/app_config.py` to modify:
  - Application registry
  - UI configuration
  - Navigation settings
  - Theme colors

#### Layout
- Modify `NAVIGATION_CONFIG` in `app_config.py` to change:
  - Cards per row
  - Card height
  - Sidebar options

## Features in Detail

### Daily Incident Outlier Report
- **Outlier Detection**: Automatically identifies unusual incident patterns
- **Interactive Charts**: Plotly-based visualizations
- **Filtering**: Date range, team, and category filters
- **Export**: CSV download functionality

### Weekly Feature Report
- **Feature Tracking**: Monitor open features and their progress
- **Status Management**: Track feature status across teams
- **Timeline View**: Gantt-like visualization of feature timelines
- **Aging Analysis**: Identify long-running features

### Monthly OPL Report
- **Performance Metrics**: Comprehensive operational performance analysis
- **Action Items**: Track action items and completion rates
- **Risk Assessment**: Identify high-risk areas
- **Financial Impact**: ROI and budget variance analysis

### Utilization Report
- **Resource Monitoring**: CPU, Memory, Storage, Network, Database utilization
- **Cost Analysis**: Cost tracking and optimization recommendations
- **Alerts**: Automatic threshold-based alerts
- **Heatmaps**: Server performance visualization

## Technical Details

### Architecture
- **Modular Design**: Each application is independent
- **Dynamic Loading**: Applications are loaded dynamically at runtime
- **Session State**: Proper state management for navigation
- **Error Handling**: Graceful error handling and user feedback

### Dependencies
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computing

### Configuration Management
- **Centralized Config**: All settings in `app_config.py`
- **Easy Registration**: Simple application registration process
- **Flexible Categories**: Organize applications by category

## Deployment

### Local Development
```bash
streamlit run main.py
```

### Production Deployment
1. **Streamlit Cloud**: Deploy directly to Streamlit Cloud
2. **Docker**: Containerize the application
3. **Cloud Platforms**: Deploy to AWS, Azure, or GCP

### Environment Variables
For production, consider setting:
- `STREAMLIT_SERVER_PORT`
- `STREAMLIT_SERVER_ADDRESS`
- Database connection strings (if using external data)

## Troubleshooting

### Common Issues

1. **Module Import Errors**
   - Ensure all `__init__.py` files are present
   - Check Python path configuration

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Port Already in Use**
   ```bash
   streamlit run main.py --server.port 8502
   ```

4. **Application Not Loading**
   - Check the module path in `app_config.py`
   - Ensure the `main()` function exists in your app

### Debug Mode
Run with debug logging:
```bash
streamlit run main.py --logger.level debug
```

## Contributing

### Adding New Features
1. Create feature branch
2. Add your application following the structure
3. Update configuration
4. Test thoroughly
5. Submit pull request

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include error handling

## Support

For support or questions:
- Check the troubleshooting section
- Review the application logs
- Contact the ISCFIT support team

## License

This project is proprietary to ISCFIT Platform.

---

**Version**: 1.0.0  
**Last Updated**: October 2024  
**Maintainer**: ISCFIT Development Team