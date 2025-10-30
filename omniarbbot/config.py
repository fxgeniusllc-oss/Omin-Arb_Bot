"""
Configuration Manager for OmniArbBot

Handles loading and validation of configuration from environment variables
and configuration files.
"""

import os
from typing import List, Optional
from dotenv import load_dotenv


class Config:
    """Configuration manager for OmniArbBot"""
    
    def __init__(self):
        """Initialize configuration from environment variables"""
        load_dotenv()
        
        # RPC Endpoints
        self.rpc_endpoints: List[str] = self._parse_list(
            os.getenv("RPC_ENDPOINTS", "")
        )
        
        # Wallet Configuration
        self.private_key: Optional[str] = os.getenv("PRIVATE_KEY")
        
        # Trading Parameters
        self.min_profit_threshold: float = float(
            os.getenv("MIN_PROFIT_THRESHOLD", "0.01")
        )
        self.max_trade_amount: float = float(
            os.getenv("MAX_TRADE_AMOUNT", "1.0")
        )
        self.gas_limit: int = int(os.getenv("GAS_LIMIT", "300000"))
        
        # Bot Settings
        self.scan_interval: int = int(os.getenv("SCAN_INTERVAL", "5"))
        self.enable_auto_trading: bool = os.getenv(
            "ENABLE_AUTO_TRADING", "false"
        ).lower() == "true"
    
    def _parse_list(self, value: str) -> List[str]:
        """Parse comma-separated list from string"""
        if not value:
            return []
        return [item.strip() for item in value.split(",") if item.strip()]
    
    def validate(self) -> bool:
        """Validate configuration"""
        if not self.rpc_endpoints:
            print("Warning: No RPC endpoints configured")
            return False
        
        if self.enable_auto_trading and not self.private_key:
            print("Error: Private key required for auto trading")
            return False
        
        return True
    
    def __repr__(self) -> str:
        """String representation (hiding sensitive data)"""
        return (
            f"Config(endpoints={len(self.rpc_endpoints)}, "
            f"auto_trading={self.enable_auto_trading}, "
            f"min_profit={self.min_profit_threshold})"
        )
