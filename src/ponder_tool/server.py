#!/usr/bin/env python3

from typing import Any, Dict, List, Optional
import json
import datetime
from mcp.server.fastmcp import FastMCP

class PonderToolServer:
    def __init__(self, server_name="ponder-tool"):
        # Initialize FastMCP server
        self.mcp = FastMCP(server_name)
        
        # Store the ponderings for logging purposes
        self.ponderings_log = []
        
        # Register tools
        self.register_tools()
    
    def register_tools(self):
        # Register the ponder tool
        @self.mcp.tool()
        async def ponder(pondering: str) -> str:
            """Use this tool to ponder about something. It will not obtain new information or change anything, 
            but just append the pondering to the log. Use it when complex reasoning or cache memory is needed.

            Args:
                pondering: A thought to ponder about. This can be structured reasoning, step-by-step analysis,
                        policy verification, or any other mental process that helps with problem-solving.
            """
            # Log the pondering with a timestamp
            timestamp = datetime.datetime.now().isoformat()
            self.ponderings_log.append({
                "timestamp": timestamp,
                "pondering": pondering
            })
            
            # Return a confirmation
            return f"Pondering recorded: {pondering[:50]}..." if len(pondering) > 50 else f"Pondering recorded: {pondering}"

        @self.mcp.tool()
        async def get_ponderings() -> str:
            """Retrieve all ponderings recorded in the current session.
            
            This tool helps review the thinking process that has occurred so far.
            """
            if not self.ponderings_log:
                return "No ponderings have been recorded yet."
            
            formatted_ponderings = []
            for i, entry in enumerate(self.ponderings_log, 1):
                formatted_ponderings.append(f"Pondering #{i} ({entry['timestamp']}):\n{entry['pondering']}\n")
            
            return "\n".join(formatted_ponderings)

        @self.mcp.tool()
        async def clear_ponderings() -> str:
            """Clear all recorded ponderings from the current session.
            
            Use this to start fresh if the thinking process needs to be reset.
            """
            count = len(self.ponderings_log)
            self.ponderings_log = []
            return f"Cleared {count} recorded ponderings."

        @self.mcp.tool()
        async def get_pondering_stats() -> str:
            """Get statistics about the ponderings recorded in the current session."""
            if not self.ponderings_log:
                return "No ponderings have been recorded yet."
            
            total_ponderings = len(self.ponderings_log)
            avg_length = sum(len(entry["pondering"]) for entry in self.ponderings_log) / total_ponderings if total_ponderings else 0
            longest_pondering = max((len(entry["pondering"]), i) for i, entry in enumerate(self.ponderings_log)) if self.ponderings_log else (0, -1)
            
            stats = {
                "total_ponderings": total_ponderings,
                "average_length": round(avg_length, 2),
                "longest_pondering_index": longest_pondering[1] + 1 if longest_pondering[1] >= 0 else None,
                "longest_pondering_length": longest_pondering[0] if longest_pondering[0] > 0 else None
            }
            
            return json.dumps(stats, indent=2)
    
    def run(self, transport='stdio'):
        """Run the server with the specified transport"""
        print(f"Starting Ponder Tool MCP Server with {transport} transport...")
        self.mcp.run(transport=transport)


def main():
    server = PonderToolServer()
    server.run()


if __name__ == "__main__":
    main()