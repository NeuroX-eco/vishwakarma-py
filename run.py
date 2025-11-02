"""
Vishwakarma AI - Application Launcher
© 2025 Vishwakarma Industries

This script launches Vishwakarma AI with multiprocessing support
for simultaneous voice assistant and hotword detection.
"""

import multiprocessing
import subprocess

def print_banner():
    """Display startup banner"""
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

# To run Vishwakarma AI
def startVishwakarma():
        print("Starting Vishwakarma AI Core...")
        from main import start
        start()

# Start application
if __name__ == '__main__':
        print_banner()
        
        try:
            startVishwakarma()
        except KeyboardInterrupt:
            print("\n\nShutdown requested by user...")
        except Exception as e:
            print(f"\n\nError occurred: {e}")
        finally:
            print("\n╔══════════════════════════════════════════════════════════════╗")
            print("║         Vishwakarma AI Shutdown Complete                    ║")
            print("║         © 2025 Vishwakarma Industries                        ║")
            print("╚══════════════════════════════════════════════════════════════╝\n")