#!/bin/bash

echo "Testing the ponder tool with Claude..."

# Create a temporary file with the test prompt
cat > /tmp/ponder_test_prompt.txt << 'EOT'
Please use the ponder tool to think through the following problem step by step:

How would you design a system to automatically categorize customer support tickets by priority and department?

After pondering, use get_ponderings to retrieve your thoughts and summarize your approach.
EOT

# Use the --print option for non-interactive mode
echo "Running Claude in non-interactive mode with the ponder tool..."
claude --print < /tmp/ponder_test_prompt.txt > /tmp/ponder_response.txt

# Display the response
echo -e "\nResponse:"
cat /tmp/ponder_response.txt

# Clean up temporary files
rm /tmp/ponder_test_prompt.txt /tmp/ponder_response.txt

echo -e "\nTest completed."