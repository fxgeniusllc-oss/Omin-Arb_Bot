"""
Sense Module - The Eyes and Ears of OmniArbBot

This module continuously monitors decentralized markets, gathering real-time
data on prices, liquidity, and trading opportunities across multiple chains.
"""

import asyncio
import time
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class MarketData:
    """Represents market data from a specific exchange/chain"""
    chain_id: str
    token_pair: str
    price: float
    liquidity: float
    timestamp: float = field(default_factory=time.time)
    
    def __repr__(self) -> str:
        return f"MarketData({self.chain_id}/{self.token_pair}: ${self.price:.6f})"


class SenseModule:
    """
    The sensing component of the neural orchestrator.
    
    Continuously monitors decentralized markets and gathers intelligence
    about trading opportunities across multiple chains and protocols.
    """
    
    def __init__(self, rpc_endpoints: List[str]):
        """
        Initialize the sense module.
        
        Args:
            rpc_endpoints: List of RPC endpoints to monitor
        """
        self.rpc_endpoints = rpc_endpoints
        self.market_data: Dict[str, MarketData] = {}
        self.is_active = False
        
    async def activate(self):
        """Activate the sensing system"""
        self.is_active = True
        print("🔍 Sense Module activated - Neural sensors online")
        
    async def deactivate(self):
        """Deactivate the sensing system"""
        self.is_active = False
        print("🔍 Sense Module deactivated")
        
    async def scan_markets(self) -> List[MarketData]:
        """
        Scan all configured markets for current state.
        
        Returns:
            List of market data from all monitored sources
        """
        if not self.is_active:
            return []
        
        # Simulate market scanning (in production, this would query actual DEXs)
        print("🔍 Scanning decentralized markets...")
        
        # Placeholder: In production, this would connect to DEXs via Web3
        market_samples = [
            MarketData(
                chain_id="eth",
                token_pair="ETH/USDC",
                price=2000.50,
                liquidity=1000000.0
            ),
            MarketData(
                chain_id="bsc",
                token_pair="ETH/USDC",
                price=2001.25,
                liquidity=500000.0
            ),
        ]
        
        # Update internal cache
        for data in market_samples:
            key = f"{data.chain_id}:{data.token_pair}"
            self.market_data[key] = data
        
        return market_samples
    
    async def monitor_continuously(self, interval: int = 5):
        """
        Continuously monitor markets at specified interval.
        
        Args:
            interval: Seconds between scans
        """
        while self.is_active:
            await self.scan_markets()
            await asyncio.sleep(interval)
    
    def get_latest_data(self) -> Dict[str, MarketData]:
        """Get the latest cached market data"""
        return self.market_data.copy()
    
    def __repr__(self) -> str:
        status = "ACTIVE" if self.is_active else "INACTIVE"
        return f"SenseModule(endpoints={len(self.rpc_endpoints)}, status={status})"
