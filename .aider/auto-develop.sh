#!/bin/bash
# Auto-develop script - Runs in background and processes commands from Ploppy Web

echo "🤖 Starting Aider Auto-Development Service..."

# Start the Aider API server
echo "🌐 Starting Aider API server on port 8080..."
python3 .aider/aider-server.py &
API_PID=$!

# Function to process commands from queue
process_commands() {
  QUEUE_FILE=".aider/command-queue.txt"
  PROCESSING_FILE=".aider/processing.lock"
  
  while true; do
    if [ -f "$QUEUE_FILE" ] && [ -s "$QUEUE_FILE" ] && [ ! -f "$PROCESSING_FILE" ]; then
      # Lock the processing
      touch "$PROCESSING_FILE"
      
      # Get the first command
      COMMAND=$(head -n 1 "$QUEUE_FILE")
      
      if [ ! -z "$COMMAND" ]; then
        echo "📝 Processing command: $COMMAND"
        
        # Remove timestamp if present
        CLEAN_COMMAND=$(echo "$COMMAND" | sed 's/^\[[^]]*\] //')
        
        # Execute with Aider using Qwen 2.5 Coder 32B
        echo "$CLEAN_COMMAND" | aider --yes-always --auto-commits
        
        # Remove processed command
        tail -n +2 "$QUEUE_FILE" > "$QUEUE_FILE.tmp"
        mv "$QUEUE_FILE.tmp" "$QUEUE_FILE"
        
        # Log completion
        echo "[$(date)] Completed: $CLEAN_COMMAND" >> .aider/completed-commands.log
      fi
      
      # Unlock
      rm -f "$PROCESSING_FILE"
    fi
    
    # Check every 5 seconds
    sleep 5
  done
}

# Function to sync with GitHub
sync_with_github() {
  while true; do
    # Pull any new commands from GitHub
    git pull --quiet
    
    # Push any changes
    if [ -n "$(git status --porcelain)" ]; then
      git add .
      git commit -m "Auto-sync from Codespace" --quiet || true
      git push --quiet || true
    fi
    
    # Sync every 30 seconds
    sleep 30
  done
}

# Start background processes
process_commands &
PROCESS_PID=$!

sync_with_github &
SYNC_PID=$!

echo "✅ Auto-development service started!"
echo "   - API Server PID: $API_PID"
echo "   - Command Processor PID: $PROCESS_PID"
echo "   - GitHub Sync PID: $SYNC_PID"

# Keep the script running
wait
