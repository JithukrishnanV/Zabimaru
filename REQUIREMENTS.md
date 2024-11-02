


Prerequisites
Python 3.7+: Ensure Python 3.7 or later is installed on your system.

Download and install Python: https://www.python.org/downloads/.
Verify the installation by running:
bash
Copy code
python --version
PowerShell (for Windows): PowerShell is required to run Zabimaru.ps1 scripts.

Pre-installed on Windows. If not, download it from https://github.com/PowerShell/PowerShell.
VirusTotal API Key: Obtain a free or paid API key from https://www.virustotal.com/.

Add your VirusTotal API key and Groq API keys to the .env file in the following format:


GQ_API_KEY="your_groqai_api_key

VT_API_KEY="your_virustotal_api_key


Installation Instructions
Clone or Download the Repository: Place ZabiApp.py, ZabimaruMain.py, and Zabimaru.ps1 in the same directory.

Create a Virtual Environment (Optional but recommended):

bash
Copy code
python -m venv .venv
source .venv/bin/activate     # On Linux/Mac
.venv\Scripts\activate        # On Windows
Install Required Libraries:

Use requirements.txt to install dependencies:
bash
Copy code
pip install -r requirements.txt
Contents of requirements.txt
plaintext
Copy code
customtkinter        # For custom UI components
Pillow               # For image handling in Tkinter
requests             # For making HTTP requests to VirusTotal API
reportlab            # For generating PDF reports
groq                 # For AI interactions (if needed)
Application Setup
Configure API Keys:

Update ZabimaruMain.py with your VirusTotal API key(s) as per the setup in get_virus_details.
Multiple API keys may be provided to handle rate limits more effectively.
Running the Application:

To start the main application, run ZabimaruMain.py:
bash
Copy code
python ZabimaruMain.py
Testing PowerShell Script Execution (Optional):

To run Zabimaru.ps1 independently, execute:
powershell
Copy code
powershell.exe -ExecutionPolicy Bypass -File "path\to\Zabimaru.ps1"
Notes
Running as an Executable: If you package this application into an .exe, ensure the PowerShell script is accessible within the executable’s environment.
Updating Dependencies: If there are additional dependencies later, add them to requirements.txt and rerun pip install -r requirements.txt.
