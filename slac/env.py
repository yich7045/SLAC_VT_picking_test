import gym
import minitouch.env

def make_dmc():
    env = gym.make("PickingDebug-v0")
    return env
