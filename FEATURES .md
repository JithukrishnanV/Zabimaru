
# Zabimaru - Features Documentation

## Overview
**Zabimaru** is a malware analysis tool designed to enhance the identification and reporting of persistent malware in Windows systems. This document outlines the primary features and includes code snippets and links to relevant images showcasing the tool's capabilities.

## Features

### 1. Application Startup Scan
Zabimaru scans for applications configured to run at startup, allowing users to identify potentially malicious software.

  ```python
  subprocess.run(
      ["powershell.exe", "-ExecutionPolicy", "Bypass", ps1_script_path, "-OutputFilePath", temp_file_path],
      check=True
  )
  ```
 ![Startup Scan](https://github.com/jithukv143/j/blob/master/Startup%20Scan.png)

### 2. Hash Calculation
The tool computes the hash of each identified startup application for further verification.

  ```python
  new_hashes_string = file.read().strip()
  new_hashes_list = new_hashes_string.split(',')
  ```


### 3. VirusTotal Integration
Zabimaru sends the computed hashes to VirusTotal and retrieves a comprehensive report on detected malware.

www.virustotal.com


  ```python
  url = f'https://www.virustotal.com/api/v3/files/{hash_value}'
  headers = {'x-apikey': VT_API_KEY}
  response = requests.get(url, headers=headers)
  ```
 ![VirusTotal Integration](https://github.com/jithukv143/j/blob/master/virustotal.png)

### 4. AI-Powered Analysis Report
Zabimaru uses Groq AI to analyze the findings from VirusTotal and generate a detailed, well-structured report.

https://groq.com/


  ```python
  completion = client.chat.completions.create(
      model="llama-3.1-70b-versatile",
      messages=[
          {
              "role": "user",
              "content": (
              "Analyze the following malware data from a VirusTotal scan report. Provide a summary..."
              )
          }
      ],
      temperature=1,
      max_tokens=1024,
      top_p=1,
      stream=True,
      stop=None,
  )
  ```
 ![AI-Powered Report](https://github.com/jithukv143/j/blob/master/groq2.png)

### 5. CustomTkinter User Interface
The tool features a user-friendly interface designed with CustomTkinter, making it accessible for both novice and expert users.

  ```python
  result_window = CTkToplevel(win)
  ```
- ![UI](https://github.com/jithukv143/j/blob/master/tkinter.png)

### 6. PDF Report Generation
Generates a PDF report summarizing the malware analysis results using the `reportlab` library.

  ```python
  pdf = canvas.Canvas(pdf_path, pagesize=letter)
  pdf.setTitle("Malware Scan Result")
  pdf.drawString(x, y, line)
  pdf.save()
  ```
![PDF UI](https://github.com/jithukv143/j/blob/master/report.png)


Each feature works together to provide a complete malware analysis solution. The process begins with the startup scan, followed by hash calculations, VirusTotal checks, AI-powered analysis, and PDF report generation.

---



