import sys
import os

# Add src to python path
sys.path.append(os.getcwd())

try:
    print("Attempting to import marketing agent API...")
    from src.marketing_agent.api import app
    print("Successfully imported marketing agent API.")
    
    print("Attempting to compile marketing agent graph...")
    from src.marketing_agent.graph import marketing_agent_graph
    print("Successfully compiled marketing agent graph.")
    
    print("Attempting to compile social media agent graph...")
    from src.social_media_agent.graph import social_media_agent_graph
    print("Successfully compiled social media agent graph.")
    
    print("VERIFICATION SUCCESSFUL")
    
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
