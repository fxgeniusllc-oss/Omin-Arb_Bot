#!/usr/bin/env python3
"""
OmniArbBot Test Demo - Shows arbitrage detection in action
"""

import asyncio
from omniarbbot.modules import SenseModule, ThinkModule, ExecuteModule
from omniarbbot.modules.sense import MarketData


async def test_arbitrage_detection():
    """Test the complete arbitrage detection and execution pipeline"""
    
    print("=" * 60)
    print("🧪 OmniArbBot Test Demo - Arbitrage Detection")
    print("=" * 60)
    
    # Create modules
    sense = SenseModule(rpc_endpoints=["https://eth.llamarpc.com", "https://bsc-dataseed.binance.org/"])
    think = ThinkModule(min_profit_threshold=0.005)  # 0.5% minimum
    execute = ExecuteModule(auto_trading=False)
    
    # Activate
    print("\n1️⃣ Activating neural modules...")
    await sense.activate()
    await think.activate()
    await execute.activate()
    
    # Inject test market data with arbitrage opportunity
    print("\n2️⃣ Injecting test market data...")
    test_markets = [
        MarketData(chain_id="ethereum", token_pair="ETH/USDC", price=2000.00, liquidity=1000000.0),
        MarketData(chain_id="bsc", token_pair="ETH/USDC", price=2015.00, liquidity=500000.0),  # 0.75% higher
        MarketData(chain_id="polygon", token_pair="BTC/USDT", price=45000.00, liquidity=2000000.0),
        MarketData(chain_id="arbitrum", token_pair="BTC/USDT", price=45500.00, liquidity=800000.0),  # 1.11% higher
    ]
    
    for market in test_markets:
        print(f"   📊 {market}")
    
    # Analyze for opportunities
    print("\n3️⃣ Analyzing for arbitrage opportunities...")
    opportunities = think.analyze_markets(test_markets)
    
    if opportunities:
        print(f"\n✨ Found {len(opportunities)} arbitrage opportunities!")
        for i, opp in enumerate(opportunities, 1):
            print(f"\n   Opportunity #{i}:")
            print(f"   Buy:  {opp.buy_market}")
            print(f"   Sell: {opp.sell_market}")
            print(f"   Profit: {opp.profit_percentage:.2f}% (${opp.estimated_profit:.2f})")
    else:
        print("   ❌ No opportunities found (profit threshold not met)")
    
    # Execute opportunities
    if opportunities:
        print("\n4️⃣ Executing trades...")
        for opp in opportunities:
            result = await execute.execute_opportunity(opp)
            print(f"   📈 {result}")
    
    # Show statistics
    print("\n5️⃣ Statistics:")
    print(f"   Think Module: {think.get_statistics()}")
    print(f"   Execute Module: {execute.get_statistics()}")
    
    # Deactivate
    print("\n6️⃣ Deactivating modules...")
    await sense.deactivate()
    await think.deactivate()
    await execute.deactivate()
    
    print("\n" + "=" * 60)
    print("✅ Test completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_arbitrage_detection())
