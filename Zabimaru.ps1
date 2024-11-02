param (
    [string]$OutputFilePath
)

# Store startup commands in a variable instead of Application-List.txt
$applicationList = Get-CimInstance Win32_StartupCommand | 
    Where-Object { $_.Command -match '\\[^\\]+\.exe' } | 
    ForEach-Object {
        $command = $_.Command -replace '^\"', '' -replace '(\s--.*|\s/.*|"\s.*|"\s*$)', ''
        if ($command -like 'C:*') { $command }
    }

# Get hashes for each application in $applicationList
$currentHashes = foreach ($line in $applicationList) {
    if (Test-Path -Path $line) {
        (Get-FileHash -Path $line -Algorithm SHA256).Hash
    }
}

# Load default hashes to compare against
$defaultHashes = Get-Content -Path "Default-hash.txt" -ErrorAction SilentlyContinue

# Check if default hashes exist
if (-Not $defaultHashes) {
    # If default hashes don't exist, set current hashes as the default
    $defaultHashes = $currentHashes
} 

# Filter hashes that don’t match the default hashes
$newHashes = foreach ($hash in $currentHashes) {
    if (-Not ($hash -in $defaultHashes)) {
        $hash
    }
}
# Join new hashes into a single string for easy output
$newHashesString = $newHashes -join ","

# Write new hashes to the specified output file
Set-Content -Path $OutputFilePath -Value $newHashesString

# Also output the new hashes to the console
#Write-Output $newHashesString
