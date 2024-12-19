# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for a ABB GoFa robot."""


import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAACLAB_NUCLEUS_DIR

##
# Configuration
##

GOFA_CONFIG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"C:/Projects/Reetz/ABBGoFa.usd", # TODO get this with less brittle method
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={"J1": 0.0, 
                   "J2": 0.0,
                   "J3": 0.0,
                    "J4": 0.0,
                    "J5": 0.0,
                    "J6": 0.0
                   }
    ),
    actuators={
        "joints": ImplicitActuatorCfg(
            joint_names_expr=["J[1-6]"],
            effort_limit=400.0,
            velocity_limit=1.0,
            stiffness=100.0,
            damping=10.0,
        ),
    },
)
"""Configuration for an ABB GoFa robot."""
