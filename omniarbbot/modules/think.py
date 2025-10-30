"""
Think Module - The Brain of OmniArbBot

This module analyzes market data, identifies arbitrage opportunities,
and calculates optimal trading strategies with precision and speed.
"""

from typing import List, Optional
from dataclasses import dataclass
from .sense import MarketData


@dataclass
class ArbitrageOpportunity:
    """Represents a detected arbitrage opportunity"""
    buy_market: MarketData
    sell_market: MarketData
    profit_percentage: float
    estimated_profit: float
    
    def __repr__(self) -> str:
        return (
            f"ArbitrageOpportunity({self.buy_market.chain_id} -> "
            f"{self.sell_market.chain_id}: +{self.profit_percentage:.2f}%)"
        )


class ThinkModule:
    """
    The thinking component of the neural orchestrator.
    
    Analyzes market data with machine-learning inspired algorithms
    to identify profitable arbitrage opportunities with precision.
    """
    
    def __init__(self, min_profit_threshold: float = 0.01):
        """
        Initialize the think module.
        
        Args:
            min_profit_threshold: Minimum profit percentage to consider (0.01 = 1%)
        """
        self.min_profit_threshold = min_profit_threshold
        self.is_active = False
        self.opportunities_found = 0
        
    async def activate(self):
        """Activate the thinking system"""
        self.is_active = True
        print("🧠 Think Module activated - Neural analysis online")
        
    async def deactivate(self):
        """Deactivate the thinking system"""
        self.is_active = False
        print("🧠 Think Module deactivated")
        
    def analyze_markets(self, market_data: List[MarketData]) -> List[ArbitrageOpportunity]:
        """
        Analyze market data to identify arbitrage opportunities.
        
        Args:
            market_data: List of market data to analyze
            
        Returns:
            List of identified arbitrage opportunities
        """
        if not self.is_active or len(market_data) < 2:
            return []
        
        opportunities = []
        
        # Compare all pairs of markets for the same token pair
        for i in range(len(market_data)):
            for j in range(i + 1, len(market_data)):
                market_a = market_data[i]
                market_b = market_data[j]
                
                # Only compare same token pairs across different chains
                if market_a.token_pair != market_b.token_pair:
                    continue
                
                if market_a.chain_id == market_b.chain_id:
                    continue
                
                # Calculate price difference
                opportunity = self._calculate_arbitrage(market_a, market_b)
                if opportunity:
                    opportunities.append(opportunity)
        
        self.opportunities_found += len(opportunities)
        
        if opportunities:
            print(f"🧠 Neural analysis: {len(opportunities)} opportunities detected")
        
        return opportunities
    
    def _calculate_arbitrage(
        self, 
        market_a: MarketData, 
        market_b: MarketData
    ) -> Optional[ArbitrageOpportunity]:
        """
        Calculate potential arbitrage between two markets.
        
        Args:
            market_a: First market
            market_b: Second market
            
        Returns:
            ArbitrageOpportunity if profitable, None otherwise
        """
        # Determine buy and sell markets
        if market_a.price < market_b.price:
            buy_market = market_a
            sell_market = market_b
        else:
            buy_market = market_b
            sell_market = market_a
        
        # Calculate profit percentage
        profit_pct = (sell_market.price - buy_market.price) / buy_market.price
        
        # Check if above threshold
        if profit_pct < self.min_profit_threshold:
            return None
        
        # Estimate profit (simplified, actual would account for gas, slippage, etc.)
        estimated_profit = profit_pct * 1000  # Assume $1000 trade
        
        return ArbitrageOpportunity(
            buy_market=buy_market,
            sell_market=sell_market,
            profit_percentage=profit_pct * 100,
            estimated_profit=estimated_profit
        )
    
    def get_statistics(self) -> dict:
        """Get thinking module statistics"""
        return {
            "active": self.is_active,
            "opportunities_found": self.opportunities_found,
            "min_profit_threshold": f"{self.min_profit_threshold * 100}%"
        }
    
    def __repr__(self) -> str:
        status = "ACTIVE" if self.is_active else "INACTIVE"
        return (
            f"ThinkModule(threshold={self.min_profit_threshold*100:.1f}%, "
            f"status={status}, found={self.opportunities_found})"
        )
