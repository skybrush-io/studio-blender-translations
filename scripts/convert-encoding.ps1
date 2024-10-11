#!/usr/bin/env pwsh

$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding($False)
foreach ($f in Get-ChildItem -Recurse) {
  if (-Not $f.PSIsContainer) {
    [System.IO.File]::WriteAllLines($f, (Get-Content $f), $Utf8NoBomEncoding)
  }
}
