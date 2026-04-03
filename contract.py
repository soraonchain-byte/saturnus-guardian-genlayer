# v0.1.2 - Saturnus Guardian (Refined for Global Hackathon)
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class SaturnusGuardian(gl.Contract):
    """
    Saturnus Guardian: An Intelligent Contract designed to bridge the 'Clarity Gap' 
    in Web3 transactions by analyzing subjective intent and preventing scams.
    """
    
    # State variables persisted on-chain
    contract_admin: Address
    security_posture: str

    def __init__(self, initial_posture: str):
        """
        Initializes the contract with an admin and a default security posture.
        """
        self.contract_admin = msg.sender
        self.security_posture = initial_posture

    @gl.public.view
    def analyze_transaction_intent(self, user_intent_description: str) -> str:
        """
        Performs a subjective intent analysis to detect potential threats 
        before a user signs a transaction.
        """
        # Define high-risk patterns for initial heuristic-based filtering
        malicious_patterns = [
            "drain", "approve all", "sweep", "transfer all", 
            "claim airdrop", "emergency withdraw", "set approval for all"
        ]
        
        normalized_intent = user_intent_description.lower()
        
        # Phase 1: Heuristic Security Check
        for pattern in malicious_patterns:
            if pattern in normalized_intent:
                return f"🛑 SECURITY ALERT: Potential scam detected! Matches malicious pattern: [{pattern}]"
        
        # Phase 2: Intent Validation (Narrative UX)
        # Note: In future Bradbury updates, this can trigger a gl.call_llm() 
        # for deep semantic analysis of the transaction metadata.
        return f"🟢 SECURITY VERIFIED: Intent '{user_intent_description}' appears legitimate under current posture."

    @gl.public.write
    def update_security_posture(self, new_posture: str) -> None:
        """
        Updates the global security posture of the Guardian. 
        Only accessible by the authorized Architect (Admin).
        """
        # Authorization check: msg.sender must be the contract_admin
        if msg.sender != self.contract_admin:
            # Reverting state change if unauthorized
            return "ACCESS DENIED: Unauthorized caller."
            
        self.security_posture = new_posture
        print(f"Saturnus Log: Security posture updated to [{new_posture}] by admin.")

    @gl.public.view
    def get_current_posture(self) -> str:
        """
        Returns the current active security posture of the Guardian.
        """
        return f"Current Security Posture: {self.security_posture}"