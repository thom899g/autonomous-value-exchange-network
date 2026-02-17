import pandas as pd
import numpy as np
from typing import Optional, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketAnalyzer:
    """Analyzes market data to identify profitable opportunities.
    
    Attributes:
        data_source: Source of market data (e.g., API, file).
        window_size: Number of periods to consider for analysis.
    """
    
    def __init__(self, data_source: str = 'api', window_size: int = 20):
        self.data_source = data_source
        self.window_size = window_size
        self._data: Optional[pd.DataFrame] = None
        
    def fetch_data(self) -> pd.DataFrame:
        """Fetches market data from the specified source."""
        try:
            # Simulated data fetching; replace with actual API calls
            self._data = pd.DataFrame({
                'price': np.random.rand(100),
                'volume': np.random.randint(100, size=100)
            })
            logger.info("Market data fetched successfully.")
            return self._data
        except Exception as e:
            logger.error(f"Failed to fetch market data: {str(e)}")
            raise MarketDataError("Market data fetching failed")
    
    def compute_trend(self) -> Dict[str, Any]:
        """Computes the trend over a specified window."""
        if self._data is None or len(self._data) < self.window_size:
            raise InsufficientDataError("Not enough data to compute trend.")
            
        try:
            # Calculate moving average
            ma = self._data['price'].rolling(self.window_size).mean()
            current_price = self._data['price'].iloc[-1]
            is_uptrend = ma[-1] > current_price
            
            return {
                'is_uptrend': is_uptrend,
                'strength': (ma[-1] - current_price) / current_price * 100
            }
        except Exception as e:
            logger.error(f"Error computing trend: {str(e)}")
            raise TrendComputationError("Failed to compute market trend.")