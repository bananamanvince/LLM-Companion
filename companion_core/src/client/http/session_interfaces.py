from flask import Flask, request, jsonify
import requests
from app.agent.agent_manager import *

"""
session http interfaces
"""

app = Flask(__name__)

@app.route('/session/create', methods = ["PUT"])
def create_session():
    """
    创建会话实例, 
    """
    return

@app.route('/session/<session_id>', methods = ["GET"])
def query_session(session_id):
    """
    查询会话实例
    """
    return

@app.route('/session/<session_id>', methods = ["POST"])
def update_session(session_id):
    """
    全量更新会话实例属性
    """
    return

@app.route('/session/<session_id>', methods = ["DELETE"])
def delete_session(session_id):
    """
    删除会话实例
    """
    return