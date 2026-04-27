#!/usr/bin/env pwsh

$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding($False)
foreach ($f in Get-ChildItem -Recurse) {
  if (-Not $f.PSIsContainer) {
    $text = [System.IO.File]::ReadAllText($f)
    [System.IO.File]::WriteAllText($f, $text, $Utf8NoBomEncoding)
  }
}
