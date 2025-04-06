import sys
import os
import numpy as np
import gymnasium as gym
import GymEnvCode.HSREnv
import time
import pygame
import keyboard
from GymEnvCode.HSREnv.envs.hsr import HSR
from GymEnvCode.HSREnv.envs.environment import Environment
import pyautogui as pg
import threading
import Interface.dataGrabber as dg
import Interface.mouseController as mc

from sb3_contrib.ppo_mask import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker
from sb3_contrib.common.maskable.policies import MaskableMultiInputActorCriticPolicy
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.evaluation import evaluate_policy
from sb3_contrib.common.maskable.utils import get_action_masks

START = False

def mask_fn(obs):
        mask = [[0,0,0,0,1,0],[1,1,1,1,1]]
        for i in range(4):
            mask[0][i] = obs["AllyUlts"][i]
        for i in range(5):
            mask[1][i] = obs["EnemyHp"][i] != 0

        mask[0][5] = obs["SkillPoints"] > 0

        flattenMask = []
        for i in mask:
            for j in i:
                flattenMask.append(j)

        return flattenMask

def actionInterpreter(act):
        action = ["ult1", "ult2", "ult3", "ult4", "basic", "skill"]
        target = [0, 1, 2, 3, 4]
        return {"action" : action[act[0]], "target" : target[act[1]]}

if __name__ == "__main__":
    controller = mc.MouseController()
        
    model = MaskablePPO.load(path="HSREnv-v2")
    dg.initSrc(["Feixiao", "Robin", "Adventurine", "March7"])
        
    while True:
        if keyboard.is_pressed('y'):
            START = not START
            print("SWITCHED TO ", START)
            time.sleep(1)
        if(START):
            try:
                obs = dg.getObs(4, debug=False, test = False)
                action, _states = model.predict(obs, action_masks=mask_fn(obs))
                ac = actionInterpreter(action)
                print(ac)
                controller.changeTarget(ac["target"])
                controller.click(ac["action"])
            except TypeError:
                time.sleep(0.5)
                continue
            
            #aaaaaaaadaaaa       ddddddcontroller.click(ac["action"])
