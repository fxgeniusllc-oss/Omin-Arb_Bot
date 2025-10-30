#!/usr/bin/env python3
"""
OmniArbBot Example - Quick Start Demo

This example demonstrates how to use OmniArbBot programmatically.
"""

import asyncio
from omniarbbot import NeuralOrchestrator
from omniarbbot.config import Config


async def example_basic_usage():
    """Example: Basic usage with default configuration"""
    print("Example 1: Basic Usage\n")
    
    # Create configuration
    config = Config()
    
    # Override some settings for demo
    config.rpc_endpoints = ["https://eth.llamarpc.com", "https://bsc-dataseed.binance.org/"]
    config.min_profit_threshold = 0.005  # 0.5%
    config.enable_auto_trading = False  # Simulation mode
    
    # Create orchestrator
    orchestrator = NeuralOrchestrator(config)
    
    # Run for 15 seconds
    await orchestrator.run(duration=15)


async def example_manual_cycle():
    """Example: Run a single cycle manually"""
    print("\n\nExample 2: Manual Cycle\n")
    
    config = Config()
    config.rpc_endpoints = ["https://eth.llamarpc.com"]
    
    orchestrator = NeuralOrchestrator(config)
    
    # Activate
    await orchestrator.activate()
    
    # Run one cycle
    print("\nRunning single cycle...")
    await orchestrator.run_cycle()
    
    # Deactivate
    await orchestrator.deactivate()
    orchestrator.print_summary()


async def example_custom_modules():
    """Example: Access individual modules"""
    print("\n\nExample 3: Individual Modules\n")
    
    from omniarbbot.modules import SenseModule, ThinkModule, ExecuteModule
    
    # Create modules individually
    sense = SenseModule(rpc_endpoints=["https://eth.llamarpc.com"])
    think = ThinkModule(min_profit_threshold=0.01)
    execute = ExecuteModule(auto_trading=False)
    
    # Activate
    await sense.activate()
    await think.activate()
    await execute.activate()
    
    # Use modules
    print("\n1. Sensing markets...")
    market_data = await sense.scan_markets()
    
    print("2. Analyzing for opportunities...")
    opportunities = think.analyze_markets(market_data)
    
    if opportunities:
        print("3. Executing top opportunity...")
        result = await execute.execute_opportunity(opportunities[0])
        print(f"   Result: {result}")
    
    # Deactivate
    await sense.deactivate()
    await think.deactivate()
    await execute.deactivate()


async def main():
    """Run all examples"""
    print("=" * 60)
    print("OmniArbBot Examples")
    print("=" * 60)
    
    # Run examples
    await example_basic_usage()
    await example_manual_cycle()
    await example_custom_modules()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
