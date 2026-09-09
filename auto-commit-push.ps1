$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

$branch = git branch --show-current
if ([string]::IsNullOrWhiteSpace($branch)) {
    throw "No se pudo determinar la rama actual."
}

git add -A

if (git diff --cached --quiet) {
    exit 0
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "Actualización automática $timestamp"
git push origin $branch