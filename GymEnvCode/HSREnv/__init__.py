from gymnasium.envs.registration import register
from GymEnvCode.HSREnv import envs
 
register(
    id='HSREnv-v2',
    entry_point='HSREnv.envs:Environment'
)
 