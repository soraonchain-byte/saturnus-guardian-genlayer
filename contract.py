from genlayer import *

class SaturnusGuardian:
    def __init__(self):
        # Inisialisasi admin kontrak dan level keamanan default
        self.admin = msg.sender
        self.security_level = "High"

    @view
    def validate_intent(self, transaction_details: str) -> str:
        """
        Menganalisis niat (intent) transaksi secara subjektif.
        Ini adalah fondasi untuk integrasi dengan LLM Jury di Testnet Bradbury.
        """
        # Daftar kata kunci yang sering dikaitkan dengan serangan drainer/sweeper
        suspicious_keywords = [
            "drain", 
            "approve all", 
            "unknown source", 
            "sweep", 
            "transfer all"
        ]
        
        # Logika validasi sederhana berbasis teks
        # Di tahap berikutnya, bagian ini akan memanggil Consensus LLM
        for word in suspicious_keywords:
            if word in transaction_details.lower():
                return f"⚠️ ALERT: Potential Clarity Gap detected! Intent '{transaction_details}' looks risky."
        
        return f"✅ Intent Validated: Transaction '{transaction_details}' matches user safety profile."

    @public
    def update_security_config(self, new_level: str):
        """
        Mengizinkan admin untuk mengubah konfigurasi keamanan kontrak.
        """
        assert msg.sender == self.admin, "Only the Guardian Admin can update config."
        self.security_level = new_level
        print(f"Security level updated to: {new_level}")
