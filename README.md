# Embedded_Systems_Copilot

# Project Setup Instructions

### To run the project, clone the repository and type the following commands in the command prompt:

1. **Create an AWS Account, activate Bedrock and create secret_key,secret_acccess_key**
   ```bash
   aws configure 
2. **Clone the repository**:
   ```bash
   git clone 
3. **Create a new conda environment**:
   ```bash
   conda create -n web python=3.10
4. **Activate the Account**:
   ```bash
   conda activate web
5. **Install the requirements.txt**
   ```bash
   pip install -r requirements.txt
6. **To run the app**
   ```bash
   streamlit run app.py
7. **After creating EC2 Instance run the following commands to make your instance upto date**
   ``bash
   sudo apt update
   sudo apt-get update
   sudo apt upgrade -y
   sudo apt install git curl unzip tar make sudo vim wget -y
   git clone "Your-repository"
   sudo apt install python3-pip
8. **For Creating new environment**
   ``bash
   sudo apt install python3-venv
   python3 -m venv .venv
   source .venv/bin/activate
9. **For installing requirements.txt**
   ``bash
   pip3 install -r requirements.txt
   #Temporary running
   python3 -m streamlit run app.py
   #Permanent running
   nohup python3 -m streamlit run app.py
