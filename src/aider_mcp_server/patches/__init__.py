"""
Patches for aider-mcp-server to ensure compatibility with Python 3.13
which has removed some previously built-in modules.
"""

import importlib
import sys
import os
import warnings
from importlib.util import find_spec

def apply_patches():
    """Apply patches to make aider work with Python 3.13."""
    # Check if audioop module exists (missing in Python 3.13)
    audioop_available = find_spec('audioop') is not None or find_spec('pyaudioop') is not None
    
    if not audioop_available:
        warnings.warn(
            "audioop module not available in this Python environment. "
            "Voice recording functionality will be disabled."
        )
        
        # Patch the voice module to handle missing audioop
        from aider_mcp_server.patches import voice
        sys.modules['aider.voice'] = voice
