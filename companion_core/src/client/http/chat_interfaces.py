from flask import Flask, request, jsonify
import requests
from app.agent.agent_manager import *

"""
chat http interfaces
"""

app = Flask(__name__)

@app.route('/chat/generate/<session_id>', methods = ["POST"])
def chat(session_id):
    """
    传入新的对话文本内容
    """
    return

@app.route('/chat/rollback/<session_id>', methods = ["POST"])
def rollback(session_id):
    """
    回滚上一轮对话
    """