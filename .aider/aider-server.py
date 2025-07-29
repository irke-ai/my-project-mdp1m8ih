#!/usr/bin/env python3
"""
Aider API Server - Enables remote control of Aider from Ploppy Web
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import threading
import queue
import os
import json
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for Ploppy Web

# Command queue
command_queue = queue.Queue()
results = {}

def execute_aider_command(cmd_id, command):
    """Execute Aider command in background"""
    try:
        # Log the command
        with open('.aider/api-commands.log', 'a') as f:
            f.write(f"[{datetime.datetime.now()}] {command}\n")
        
        # Execute with Aider using Qwen 2.5 Coder 32B
        process = subprocess.Popen(
            ['aider', '--yes-always', '--auto-commits'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=command)
        
        # Store result
        results[cmd_id] = {
            'status': 'completed',
            'output': stdout,
            'error': stderr,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
    except Exception as e:
        results[cmd_id] = {
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.datetime.now().isoformat()
        }

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'aider-api'})

@app.route('/execute', methods=['POST'])
def execute_command():
    """Execute an Aider command"""
    data = request.json
    command = data.get('command')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    # Generate command ID
    cmd_id = f"cmd_{datetime.datetime.now().timestamp()}"
    
    # Start execution in background
    thread = threading.Thread(target=execute_aider_command, args=(cmd_id, command))
    thread.start()
    
    return jsonify({
        'id': cmd_id,
        'status': 'processing',
        'message': 'Command queued for execution'
    })

@app.route('/status/<cmd_id>', methods=['GET'])
def get_status(cmd_id):
    """Get command execution status"""
    if cmd_id in results:
        return jsonify(results[cmd_id])
    else:
        return jsonify({'status': 'processing'})

@app.route('/project/info', methods=['GET'])
def project_info():
    """Get project information"""
    try:
        # Read project context
        context = {}
        if os.path.exists('PROJECT_CONTEXT.md'):
            with open('PROJECT_CONTEXT.md', 'r') as f:
                context['project_context'] = f.read()
        
        # Get recent commits
        commits = subprocess.check_output(['git', 'log', '--oneline', '-10'], text=True)
        context['recent_commits'] = commits
        
        # Get file structure
        files = subprocess.check_output(['find', '.', '-type', 'f', '-name', '*.ts', '-o', '-name', '*.tsx', '-o', '-name', '*.js', '-o', '-name', '*.jsx'], text=True)
        context['project_files'] = files.split('\n')[:50]  # First 50 files
        
        return jsonify(context)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure OpenAI API key is set
    if not os.environ.get('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not set!")
    
    print("🚀 Starting Aider API Server on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=False)
