#!/usr/bin/env python3
"""
OmniArbBot - Main Entry Point

Run the neural orchestrator to start the autonomous arbitrage bot.
"""

import asyncio
import sys
from omniarbbot import NeuralOrchestrator
from omniarbbot.config import Config


def print_banner():
    """Print the OmniArbBot banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║              🤖  O M N I A R B B O T  🤖                 ║
    ║                                                           ║
    ║           Neural Orchestrator for DeFi Trading            ║
    ║                                                           ║
    ║        Sense  →  Think  →  Execute  →  Profit            ║
    ║                                                           ║
    ║     Fast • Adaptive • Unstoppable • Autonomous           ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


async def main():
    """Main entry point"""
    print_banner()
    
    # Load configuration
    config = Config()
    
    # Validate configuration
    if not config.validate():
        print("\n❌ Configuration validation failed")
        print("\n💡 Quick Start:")
        print("   1. Copy .env.example to .env")
        print("   2. Add your RPC endpoints")
        print("   3. Configure trading parameters")
        print("   4. Run again!")
        sys.exit(1)
    
    # Create and run the neural orchestrator
    orchestrator = NeuralOrchestrator(config)
    
    # Run for 30 seconds as a demo (remove duration for continuous operation)
    await orchestrator.run(duration=30)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
