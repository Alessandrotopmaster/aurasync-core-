from core.traffic_optimizer import TrafficOptimizer
from core.split_payment import AuraSyncSplitPayment
import os
from dotenv import load_dotenv
load_dotenv()
orc = float(os.getenv("DAILY_BUDGET",50))
taxa = float(os.getenv("SYSTEM_FEE",0.05))
