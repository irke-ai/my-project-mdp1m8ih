#!/bin/bash

echo "🚀 Setting up Aider development environment..."

# Install Aider
python3 -m pip install --user aider-chat

# Create Aider config
cat > .aider.conf.yml << 'EOF'
model: gpt-4-turbo-preview
auto-commits: true
pretty: true
show-diffs: true
EOF

echo "✅ Aider setup complete!"
echo "Run 'aider' to start AI-assisted development"
