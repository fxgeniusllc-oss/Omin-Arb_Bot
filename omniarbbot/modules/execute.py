"""
Execute Module - The Hands of OmniArbBot

This module executes trades with precision across decentralized protocols,
handling transaction submission, gas optimization, and trade verification.
"""

import asyncio
import time
from typing import Optional
from dataclasses import dataclass
from .think import ArbitrageOpportunity


@dataclass
class TradeExecution:
    """Represents an executed trade"""
    opportunity: ArbitrageOpportunity
    status: str  # "pending", "success", "failed"
    tx_hash: Optional[str] = None
    gas_used: int = 0
    actual_profit: float = 0.0
    timestamp: float = 0.0
    
    def __repr__(self) -> str:
        return f"TradeExecution({self.status}, profit=${self.actual_profit:.2f})"


class ExecuteModule:
    """
    The execution component of the neural orchestrator.
    
    Executes trades with precision, speed, and safety across
    multiple decentralized protocols and chains.
    """
    
    def __init__(
        self, 
        private_key: Optional[str] = None,
        gas_limit: int = 300000,
        auto_trading: bool = False
    ):
        """
        Initialize the execute module.
        
        Args:
            private_key: Private key for transaction signing
            gas_limit: Maximum gas limit per transaction
            auto_trading: Whether to automatically execute trades
        """
        self.private_key = private_key
        self.gas_limit = gas_limit
        self.auto_trading = auto_trading
        self.is_active = False
        self.trades_executed = 0
        self.total_profit = 0.0
        
    async def activate(self):
        """Activate the execution system"""
        self.is_active = True
        mode = "AUTO" if self.auto_trading else "MANUAL"
        print(f"⚡ Execute Module activated - Trade execution online ({mode} mode)")
        
    async def deactivate(self):
        """Deactivate the execution system"""
        self.is_active = False
        print("⚡ Execute Module deactivated")
        
    async def execute_opportunity(
        self, 
        opportunity: ArbitrageOpportunity
    ) -> TradeExecution:
        """
        Execute an arbitrage opportunity.
        
        Args:
            opportunity: The arbitrage opportunity to execute
            
        Returns:
            TradeExecution result
        """
        if not self.is_active:
            return TradeExecution(
                opportunity=opportunity,
                status="failed",
                timestamp=time.time()
            )
        
        print(f"⚡ Executing: {opportunity}")
        
        # Simulate trade execution (in production, this would submit actual transactions)
        execution = TradeExecution(
            opportunity=opportunity,
            status="pending",
            timestamp=time.time()
        )
        
        if not self.auto_trading:
            print("⚡ Manual mode: Would execute trade (simulation)")
            execution.status = "simulated"
            execution.actual_profit = opportunity.estimated_profit * 0.95  # Account for fees
            return execution
        
        if not self.private_key:
            print("⚡ Error: No private key configured")
            execution.status = "failed"
            return execution
        
        # Simulate transaction submission
        await asyncio.sleep(0.5)  # Simulate network delay
        
        # In production: Submit buy transaction on buy_market
        # In production: Submit sell transaction on sell_market
        
        execution.status = "success"
        execution.tx_hash = f"0x{'a' * 64}"  # Mock transaction hash
        execution.gas_used = 200000
        execution.actual_profit = opportunity.estimated_profit * 0.92  # Account for gas & fees
        
        self.trades_executed += 1
        self.total_profit += execution.actual_profit
        
        print(f"⚡ Trade executed successfully! Profit: ${execution.actual_profit:.2f}")
        
        return execution
    
    async def execute_batch(
        self, 
        opportunities: list
    ) -> list:
        """
        Execute multiple opportunities in batch.
        
        Args:
            opportunities: List of arbitrage opportunities
            
        Returns:
            List of trade executions
        """
        executions = []
        for opportunity in opportunities:
            execution = await self.execute_opportunity(opportunity)
            executions.append(execution)
            # Small delay between trades to avoid nonce conflicts
            await asyncio.sleep(0.1)
        
        return executions
    
    def get_statistics(self) -> dict:
        """Get execution module statistics"""
        return {
            "active": self.is_active,
            "auto_trading": self.auto_trading,
            "trades_executed": self.trades_executed,
            "total_profit": f"${self.total_profit:.2f}",
            "avg_profit": f"${self.total_profit / max(1, self.trades_executed):.2f}"
        }
    
    def __repr__(self) -> str:
        status = "ACTIVE" if self.is_active else "INACTIVE"
        mode = "AUTO" if self.auto_trading else "MANUAL"
        return (
            f"ExecuteModule(mode={mode}, status={status}, "
            f"executed={self.trades_executed}, profit=${self.total_profit:.2f})"
        )
