"""
Vishwakarma AI - Application Launcher
© 2025 Vishwakarma Industries

This script launches the Vishwakarma AI application.
"""
import sys

def print_banner():
    """Displays the startup banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              VISHWAKARMA AI - VERSION 1.0.0                  ║
    ║                                                              ║
    ║              Intelligent Voice Assistant                     ║
    ║                                                              ║
    ║              © 2025 Vishwakarma Industries                   ║
    ║              All Rights Reserved                             ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    
    Initializing Vishwakarma AI...
    """
    print(banner)

def start_vishwakarma():
    """Starts the main application."""
    print("Starting Vishwakarma AI Core...")
    try:
        from main import start
        start()
    except ImportError as e:
        print(f"Error importing main module: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during startup: {e}")
        sys.exit(1)

def main():
    """The main entry point of the application."""
    print_banner()

    try:
        start_vishwakarma()
    except KeyboardInterrupt:
        print("\n\nShutdown requested by user...")
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
    finally:
        print("\n╔══════════════════════════════════════════════════════════════╗")
        print("║         Vishwakarma AI Shutdown Complete                    ║")
        print("║         © 2025 Vishwakarma Industries                        ║")
        print("╚══════════════════════════════════════════════════════════════╝\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
