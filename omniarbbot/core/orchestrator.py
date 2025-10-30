"""
Neural Orchestrator - The Heart of OmniArbBot

The central intelligence that coordinates the Sense, Think, and Execute modules
to create a seamless, autonomous trading system.
"""

import asyncio
from typing import Optional
from ..config import Config
from ..modules.sense import SenseModule
from ..modules.think import ThinkModule
from ..modules.execute import ExecuteModule


class NeuralOrchestrator:
    """
    The neural orchestrator is the digital nervous system of OmniArbBot.
    
    It coordinates all three core modules:
    - Sense: Monitors markets and gathers data
    - Think: Analyzes data and identifies opportunities
    - Execute: Executes trades with precision
    
    Together, they form an intelligent, adaptive, and unstoppable arbitrage engine.
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the neural orchestrator.
        
        Args:
            config: Configuration object (uses defaults if None)
        """
        self.config = config or Config()
        
        # Initialize the three neural modules
        self.sense = SenseModule(rpc_endpoints=self.config.rpc_endpoints)
        self.think = ThinkModule(
            min_profit_threshold=self.config.min_profit_threshold
        )
        self.execute = ExecuteModule(
            private_key=self.config.private_key,
            gas_limit=self.config.gas_limit,
            auto_trading=self.config.enable_auto_trading
        )
        
        self.is_running = False
        self._tasks = []
        
    async def activate(self):
        """Activate the neural orchestrator and all its modules"""
        print("=" * 60)
        print("🤖 OmniArbBot Neural Orchestrator - Initializing")
        print("=" * 60)
        print(f"Configuration: {self.config}")
        print()
        
        # Activate all modules
        await self.sense.activate()
        await self.think.activate()
        await self.execute.activate()
        
        self.is_running = True
        
        print()
        print("✅ Neural orchestrator activated - All systems online")
        print("🚀 Digital nervous system operational - Fast, adaptive, unstoppable")
        print("=" * 60)
        
    async def deactivate(self):
        """Deactivate the neural orchestrator and all its modules"""
        print("\n🛑 Shutting down neural orchestrator...")
        
        self.is_running = False
        
        # Cancel all running tasks
        for task in self._tasks:
            task.cancel()
        
        # Wait for tasks to complete
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
        
        # Deactivate all modules
        await self.sense.deactivate()
        await self.think.deactivate()
        await self.execute.deactivate()
        
        print("✅ Neural orchestrator deactivated")
        
    async def run_cycle(self):
        """
        Run a single cycle of the neural orchestrator:
        1. Sense - Scan markets
        2. Think - Analyze for opportunities
        3. Execute - Execute profitable trades
        """
        if not self.is_running:
            return
        
        # SENSE: Gather market intelligence
        market_data = await self.sense.scan_markets()
        
        if not market_data:
            return
        
        # THINK: Analyze for arbitrage opportunities
        opportunities = self.think.analyze_markets(market_data)
        
        if not opportunities:
            return
        
        # EXECUTE: Execute the most profitable opportunities
        for opportunity in opportunities[:3]:  # Limit to top 3
            await self.execute.execute_opportunity(opportunity)
    
    async def run_continuous(self):
        """
        Run the neural orchestrator continuously.
        
        The bot will continuously sense, think, and execute in an infinite loop
        until deactivated.
        """
        print(f"\n🔄 Starting continuous operation (scan interval: {self.config.scan_interval}s)")
        
        while self.is_running:
            try:
                await self.run_cycle()
                await asyncio.sleep(self.config.scan_interval)
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"⚠️  Error in cycle: {e}")
                await asyncio.sleep(self.config.scan_interval)
    
    async def run(self, duration: Optional[int] = None):
        """
        Run the neural orchestrator.
        
        Args:
            duration: Optional duration in seconds (runs indefinitely if None)
        """
        await self.activate()
        
        try:
            if duration:
                # Run for specified duration
                print(f"\n⏱️  Running for {duration} seconds...")
                await asyncio.wait_for(
                    self.run_continuous(), 
                    timeout=duration
                )
            else:
                # Run indefinitely
                await self.run_continuous()
        except asyncio.TimeoutError:
            print(f"\n⏱️  Duration complete")
        except KeyboardInterrupt:
            print("\n⏱️  Interrupted by user")
        finally:
            await self.deactivate()
            self.print_summary()
    
    def print_summary(self):
        """Print summary statistics"""
        print("\n" + "=" * 60)
        print("📊 Session Summary")
        print("=" * 60)
        
        think_stats = self.think.get_statistics()
        exec_stats = self.execute.get_statistics()
        
        print(f"Opportunities Found: {think_stats['opportunities_found']}")
        print(f"Trades Executed: {exec_stats['trades_executed']}")
        print(f"Total Profit: {exec_stats['total_profit']}")
        print(f"Average Profit: {exec_stats['avg_profit']}")
        print("=" * 60)
    
    def __repr__(self) -> str:
        status = "RUNNING" if self.is_running else "STOPPED"
        return f"NeuralOrchestrator(status={status}, modules=3)"
