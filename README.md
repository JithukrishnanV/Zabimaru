![repository-open-graph](https://github.com/jithukv143/j/blob/master/Logod.png)
# Zabimaru

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://choosealicense.com/licenses/mit/)



`ZABIMARU`  is a comprehensive malware analysis tool designed to identify and report persistent malware on Windows systems. The tool scans for running services and startup applications, hashes their executable files, and checks them against VirusTotal. Any detected malicious files are then analyzed using Groq AI to generate a detailed malware analysis report. The tool includes a user-friendly UI built using CustomTkinter for seamless interaction.

It has a boatload of features, see [FEATURES.md](FEATURES.md)



## Requirements
* Python 3.x
Libraries:
*     -requests
*     -dotenv
*     -reportlab
*     -groq
External Tools:
*     -PowerShell for executing scripts that retrieve running services and startup programs.

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/zabimaru.git
cd zabimaru
```

### 2. Install the required Python packages:


```bash
pip install -r requirements.txt

```

### 3. Create a key.env file and provide your API keys:

```bash
GQ_API_KEY="your_groq_api_key"
VT_API_KEY="your_virustotal_api_key"

```
### 4. Run ZabiMain.py

```bash
.\ZabimaruMain.py
```


## How Zabimaru Works?

* Running the PowerShell Script: Zabimaru runs a bundled PowerShell script (Zabimaru.ps1) to gather running services and startup applications.

* Hashing and Analysis:

    * The tool computes hashes of the detected applications and checks these hashes against VirusTotal.
    * If malicious entries are found, Groq AI generates a detailed analysis report.
        Generating a PDF Report:

* The analysis results are saved in a user-readable PDF file using the reportlab library.

## Usage

Run the tool with:

```bash
python ZabimaruMain.py
```

## Disclaimer

Zabimaru is intended for educational and research purposes only. Ensure you use it in a controlled, isolated environment and comply with relevant laws and regulations when handling malware.

Click here too see results [results.md](results.md)

![PDF UI](https://github.com/jithukv143/j/blob/master/result.png)
