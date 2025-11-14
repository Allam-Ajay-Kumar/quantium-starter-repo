# Activate virtual environment
. .\venv\Scripts\Activate.ps1

# Run tests
pytest

# Check pytest exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Host "Some tests failed."
    exit 1
}
