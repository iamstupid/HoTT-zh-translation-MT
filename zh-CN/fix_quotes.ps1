# PowerShell script to convert straight quotes to Chinese curly quotes
# Run with: powershell -ExecutionPolicy Bypass -File fix_quotes.ps1

$files = Get-ChildItem -Path $PSScriptRoot -Recurse -Filter "*.tex"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalCount = ([regex]::Matches($content, '"')).Count

    if ($originalCount -gt 0) {
        $result = New-Object System.Text.StringBuilder

        for ($i = 0; $i -lt $content.Length; $i++) {
            $char = $content[$i]
            if ($char -eq '"') {
                # Check context to determine opening/closing
                if ($i -gt 0) {
                    $prevChar = $content[$i-1]
                } else {
                    $prevChar = ' '
                }

                # Opening: after whitespace, punctuation, or opening brackets
                if ($prevChar -match '[\s（\(\[\{【「『，。！？；：、]') {
                    [void]$result.Append([char]0x201C)  # "
                } else {
                    [void]$result.Append([char]0x201D)  # "
                }
            } else {
                [void]$result.Append($char)
            }
        }

        $newContent = $result.ToString()
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        $newCount = ([regex]::Matches($newContent, '"')).Count
        Write-Host "Processed: $($file.Name) - converted $($originalCount - $newCount) quotes"
    }
}
Write-Host "Done!"
