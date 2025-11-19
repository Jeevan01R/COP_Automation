"""
Launch script for ISCFIT Platform Reporting Cockpit
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit',
        'pandas', 
        'plotly',
        'numpy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_requirements():
    """Install missing requirements"""
    print("Installing required packages...")
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def launch_application():
    """Launch the Streamlit application"""
    main_file = Path(__file__).parent / "main.py"
    
    print("🚀 Launching ISCFIT Platform Reporting Cockpit...")
    print("📍 Application will be available at: http://localhost:8501")
    print("🔄 Press Ctrl+C to stop the application")
    print("-" * 60)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(main_file),
            "--server.headless", "true",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Failed to launch application: {e}")

def main():
    """Main launcher function"""
    print("=" * 60)
    print("🎯 ISCFIT PLATFORM REPORTING COCKPIT")
    print("=" * 60)
    
    # Check for missing requirements
    missing = check_requirements()
    
    if missing:
        print(f"⚠️  Missing packages: {', '.join(missing)}")
        install_choice = input("📦 Install missing packages? (y/n): ").strip().lower()
        
        if install_choice in ['y', 'yes']:
            if not install_requirements():
                print("❌ Cannot proceed without required packages.")
                sys.exit(1)
        else:
            print("❌ Cannot proceed without required packages.")
            sys.exit(1)
    else:
        print("✅ All requirements satisfied!")
    
    # Launch the application
    launch_application()

if __name__ == "__main__":
    main()