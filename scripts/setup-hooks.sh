#!/usr/bin/env bash
# Install git hooks for the repository
set -e

HOOKS_DIR="$(git rev-parse --show-toplevel)/.git/hooks"

cat << 'EOF' > "$HOOKS_DIR/pre-commit"
#!/bin/sh
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# 1. Protect main branch
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    echo "ERROR: Direct commits to '$BRANCH' are strictly forbidden!"
    echo "Create a branch: git checkout -b feat/<yourname>-<topic>"
    exit 1
fi

# 2. Enforce branch naming convention
VALID_PATTERN="^(feat|fix|docs|refactor|test|chore)/(kalab|bartek|kamil)-[a-z0-9-]+$"
if ! echo "$BRANCH" | grep -Eq "$VALID_PATTERN"; then
    echo "WARNING: Branch '$BRANCH' does not match '<type>/<contributor>-<topic>'"
    echo "Allowed contributors: kalab, bartek, kamil"
fi

# 3. Prevent committing secrets
for FILE in $(git diff --cached --name-only); do
    if echo "$FILE" | grep -Eq "\.env$|\.env\.local$|credentials|secret"; then
        echo "ERROR: Attempting to commit secrets: $FILE"
        exit 1
    fi
done

# 4. Mex contract reminder
SRC_CHANGED=$(git diff --cached --name-only | grep -E "^src/" || true)
MEX_CHANGED=$(git diff --cached --name-only | grep -E "^\.mex/" || true)
if [ -n "$SRC_CHANGED" ] && [ -z "$MEX_CHANGED" ]; then
    echo "REMINDER: You changed src/ without changing .mex/. Did you update architecture/conventions?"
fi

exit 0
EOF

chmod +x "$HOOKS_DIR/pre-commit"
echo "Git pre-commit hooks installed successfully!"
