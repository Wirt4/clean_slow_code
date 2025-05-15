#!/bin/bash

# Ensure a script base name is provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <script_name_without_.py> [script_args...]"
  exit 1
fi

# Extract script base name and remaining arguments
BASENAME="$1"
SCRIPT="implementations/${BASENAME}.py"
shift
SCRIPT_ARGS="$@"

# Check if the Python script exists
if [ ! -f "$SCRIPT" ]; then
  echo "Error: '$SCRIPT' does not exist."
  exit 1
fi

# Output profile file
PROFILE_OUTPUT="profiles/${BASENAME}_output.prof"

# Step 1: Run cProfile and save to .prof file
python -m cProfile -o "$PROFILE_OUTPUT" "$SCRIPT" $SCRIPT_ARGS

# Step 2: Open interactive stats viewer
python -m pstats "$PROFILE_OUTPUT"
