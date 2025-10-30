"""
OmniArbBot - Neural Orchestrator for Decentralized Trading

A precision-level autonomous arbitrage bot that senses, thinks, and executes
across decentralized ecosystems with unmatched speed and adaptability.
"""

__version__ = "1.0.0"
__author__ = "OmniArbBot Team"

from .core.orchestrator import NeuralOrchestrator
from .modules.sense import SenseModule
from .modules.think import ThinkModule
from .modules.execute import ExecuteModule

__all__ = [
    "NeuralOrchestrator",
    "SenseModule",
    "ThinkModule",
    "ExecuteModule",
]
