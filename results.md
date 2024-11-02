# Results - Zabimaru

Zabimaru has been designed to identify persistent malware within a Windows environment through comprehensive scanning and analysis. Below is a summary of the results and findings from its operation:

#### 1. Detection of Startup Persistence:

Zabimaru successfully identifies applications and services configured to run at system startup. This helps uncover potentially unwanted or malicious programs.


 ![Startup Scan](https://github.com/jithukv143/j/blob/master/Startup_Scan.png)


#### 2. Hash Analysis and VirusTotal Integration:

The tool calculates hashes for each startup application and sends them to VirusTotal for analysis. It identifies if any startup application is flagged as malicious by comparing hash data against VirusTotal’s extensive database.


 ![hash](https://github.com/jithukv143/j/blob/master/hash.png)

#### 3. AI-Generated Malware Reports:

By leveraging Groq AI, Zabimaru provides detailed, structured reports of detected malware, including the type, behaviour, detection rate, and recommended mitigation actions.


 ![AI](https://github.com/jithukv143/j/blob/master/groq2.png)


#### 4. PDF Report Creation

Zabimaru generates PDF reports summarizing the analysis, which is useful for documentation and reporting.



#### 5. User Interface and Usability
The user-friendly CustomTkinter UI ensures that even users with limited technical expertise can operate the tool efficiently.

 ![Startup Scan](https://github.com/jithukv143/j/blob/master/start.png)


Zabimaru combines the power of startup scanning, hashing, VirusTotal checks, AI analysis, and comprehensive reporting to provide an effective solution for identifying malware persistence. Its robust features make it an essential tool for cybersecurity professionals focusing on malware analysis and threat assessment.


 ![result](https://github.com/jithukv143/j/blob/master/result.png)
---

## VirusTotal Report  for Detected Malware
Below is a list of links to VirusTotal analysis reports for the detected malware:

###### 1. **Malware Hash**: `01ec7b1066df7c55e262dc375bff5fd13a1fc9706c3db4b3522ac8b9d2453b52`
   - VirusTotal Link: https://www.virustotal.com/gui/file/01ec7b1066df7c55e262dc375bff5fd13a1fc9706c3db4b3522ac8b9d2453b52/detection

###### 2. **Malware Hash**: `1e90b6fc99a908420de123418deded8d8eadf2114ac43ee1ec366681b5358c17`
   - VirusTotal Link: https://www.virustotal.com/gui/file/1e90b6fc99a908420de123418deded8d8eadf2114ac43ee1ec366681b5358c17/detection

###### 3. **Malware Hash**: `4a27e09aeb42de72b83261f3f920f80ec1f5f8fd875ef9487ee5d6f81f726fe3`
   - VirusTotal Link: https://www.virustotal.com/gui/file/4a27e09aeb42de72b83261f3f920f80ec1f5f8fd875ef9487ee5d6f81f726fe3
