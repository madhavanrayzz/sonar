# buggy_code.py
import os
import subprocess

def bad_function():
    # S1313: Hardcoded IP (Security Hotspot)
    ip = "192.168.1.100"
    
    # S2076: OS command injection
    subprocess.run("ping -c 4 " + ip, shell=True)
    
    # S1481: Unused variable
    unused_var = 42
    
    # BUG: Possible None dereference
    data = None
    print(data.upper())


def insecure_password():
    # S2066: Hardcoded credentials (Critical Security)
    password = "admin123"
    return password


def duplicate_code():
    print("Hello World! This is a test.")
    print("Hello World! This is a test.")
    print("Hello World! This is a test.")
    print("Hello World! This is a test.")
    print("Hello World! This is a test.")


if __name__ == "__main__":
    bad_function()
