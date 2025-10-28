from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from cfg import Config
config = Config()