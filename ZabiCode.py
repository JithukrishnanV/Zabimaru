import requests
import subprocess, sys
from groq import Groq
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys
import os
import tempfile
from tkinter import messagebox



if getattr(sys, 'frozen', False):  # If running as an executable
    base_path = sys._MEIPASS
else:  # If running as a script
    base_path = os.path.abspath(".")

# Set your groq API key here
groq_api_key="key"

# Set your VirusTotal API key here
VT_API_KEY = 'key'

client = Groq(api_key=groq_api_key)





def get_virus_details(hash_value):
    """
    Get detailed information about a hash using the VirusTotal API.
    """
    url = f'https://www.virustotal.com/api/v3/files/{hash_value}'
    headers = {
        'x-apikey': VT_API_KEY
    }
 
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        json_response = response.json()
        data = json_response.get('data', {}).get('attributes', {})
        malicious_count = data.get('last_analysis_stats', {}).get('malicious', 0)
        scan_results = data.get('last_analysis_results', {})
        malware_info = []
 
        if malicious_count > 0:
            # Collecting detection names from different antivirus engines
            for engine, result in scan_results.items():
                if result['category'] == 'malicious':
                    malware_info.append(f"{engine}: {result['result']}")
 
            return {
                'malicious_count': malicious_count,
                'malware_info': malware_info
            }
            
    else:
        print(f'Error fetching data for hash {hash_value}: {response.status_code}')
    
    return None
 
def analyze_hashes(hashes):
    """
    Analyze hashes from a list and get detailed information for malicious hashes.
    """
    malicious_hashes_info = {}

    # Iterate through each hash in the list
    for hash_value in hashes:
        details = get_virus_details(hash_value)
        
        # Check if the hash has malicious detections
        if details and details['malicious_count'] > 0:
            result = get_AI_result(details)
            malicious_hashes_info[hash_value] = result

    return malicious_hashes_info

def get_AI_result(details):
    malicious_count=details['malicious_count']
    formatted_data = ""
    for info in details['malware_info']:
        formatted_data += f'  - {info}\n'
    formatted_data += '\n'
    
    # Initialize info with formatted data for the message
    info = formatted_data
    
    # Run the AI model
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": (
                "Analyze the following malware data from a VirusTotal scan report. Provide a summary of the malware's type, "
                "detection rate, behavior, potential impacts, and recommended actions for mitigation. Ensure the response is "
                "concise and well-structured, prioritizing essential information for quick understanding by cybersecurity "
                "professionals. And dont give me any bold text\n\n"
                "Malware Data: " + info
            )
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    # Collect the response into the info variable
    info = ""  
    for chunk in completion:
        info += chunk.choices[0].delta.content or ""
    
    return {
                'malicious_count': malicious_count,
                'malware_info': info
            } 



def main():
    if groq_api_key == "key" or VT_API_KEY=="key":
        print("Set API keys at start of the program")
        messagebox.showinfo("API key error", "Set API keys at start of the program")
        return 1
    # Set the path to the PowerShell script
    ps1_script_path = os.path.join(base_path, 'Zabimaru.ps1').replace("\\", "/")
    
    # Create a temporary file to store the PowerShell output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file_path = temp_file.name

    try:
        # Run the PowerShell script and pass the temporary file path as an argument
        subprocess.run(
            ["powershell.exe", "-ExecutionPolicy", "Bypass", ps1_script_path, "-OutputFilePath", temp_file_path],
            check=True
        )

        # Read the output from the temporary file
        with open(temp_file_path, "r") as file:
            new_hashes_string = file.read().strip()
            new_hashes_list = new_hashes_string.split(',')

        # Manual test  
        new_hashes_list.append('d14b48bae7484afe7942b7f21830a9561e8c49cb4cf4fa9ebbc1dc5b4573a375')
        
        

       # print("Received hashes from PowerShell:", new_hashes_list)  # For debugging

        # Pass new_hashes_list directly to analyze_hashes function
        malicious_hashes_info = analyze_hashes(new_hashes_list)

        # Return the detailed information
        if malicious_hashes_info:
            malicious_hashes = list(malicious_hashes_info.keys())
            print("\nVirus found:", malicious_hashes)
            return malicious_hashes_info
        else:
            data = "No malicious hashes found."
            print(data)
            return data

    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

if __name__ == '__main__':
    main()

 

