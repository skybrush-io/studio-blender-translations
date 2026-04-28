#!/usr/bin/env pwsh

<#
  .DESCRIPTION
  Call this script from the root directory of the repository to
  strip the byte order marks from all files in the `po` folder!
#>

$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding($False)
foreach ($f in Get-ChildItem "po") {
  if (-Not $f.PSIsContainer) {
    $text = [System.IO.File]::ReadAllText($f.FullName)
    [System.IO.File]::WriteAllText($f.FullName, $text, $Utf8NoBomEncoding)
  }
}
