import yaml
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigManager:
    """Manages configuration settings for the trading system.
    
    Attributes:
        config_file: Path to the configuration file.
    """
    
    def __init__(self, config_file: str = 'config.yaml'):
        self.config_file = config_file
        self._config: Optional[Dict[str, Any]] = None
        
    def load_config(self) -> Dict[str, Any]:
        """Loads configuration settings from a YAML file."""
        try:
            with open(self.config_file, 'r') as f:
                self._config = yaml.safe_load(f)
            logger.info("Configuration loaded successfully.")
            return self._config
        except Exception as e:
            logger.error(f"Failed to load configuration: {str(e)}")
            raise ConfigurationError("Configuration loading failed.")
    
    def get_setting(self, key: str) -> Any:
        """Retrieves a specific configuration setting."""
        if not self._config:
            raise ValueError("Configuration not loaded.")
            
        return self._config.get