# PowerShell script to install git hooks
$repoRoot = (git rev-parse --show-toplevel)
$hooksDir = Join-Path $repoRoot ".git\hooks"
$preCommitPath = Join-Path $hooksDir "pre-commit"

$hookContent = @'
#!/bin/sh
BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    echo "ERROR: Direct commits to '$BRANCH' are strictly forbidden!"
    echo "Create a branch: git checkout -b feat/<yourname>-<topic>"
    exit 1
fi

VALID_PATTERN="^(feat|fix|docs|refactor|test|chore)/(kalab|bartek|kamil)-[a-z0-9-]+$"
if ! echo "$BRANCH" | grep -Eq "$VALID_PATTERN"; then
    echo "WARNING: Branch '$BRANCH' does not match '<type>/<contributor>-<topic>'"
    echo "Allowed contributors: kalab, bartek, kamil"
fi

for FILE in $(git diff --cached --name-only); do
    if echo "$FILE" | grep -Eq "\.env$|\.env\.local$|credentials|secret"; then
        echo "ERROR: Attempting to commit secrets: $FILE"
        exit 1
    fi
done

# Jev System-1 Guardrail
if command -v python &> /dev/null; then
    python scripts/jev_guardrail.py || exit 1
elif command -v python3 &> /dev/null; then
    python3 scripts/jev_guardrail.py || exit 1
fi

SRC_CHANGED=$(git diff --cached --name-only | grep -E "^src/" || true)
MEX_CHANGED=$(git diff --cached --name-only | grep -E "^\.mex/" || true)
if [ -n "$SRC_CHANGED" ] && [ -z "$MEX_CHANGED" ]; then
    echo "REMINDER: You changed src/ without changing .mex/. Did you update architecture/conventions?"
fi

exit 0
'@

Set-Content -Path $preCommitPath -Value $hookContent -Encoding ASCII
Write-Host "Git pre-commit hooks (with Jev Guardrail) installed successfully at: $preCommitPath"
