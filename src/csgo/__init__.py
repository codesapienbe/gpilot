import gymnasium as gym


def main():
    """
    The main function creates and runs an instance of the 'csgo_dm-v0' gym environment.
    No input parameters are required. No output is returned.

    The function creates an instance of the environment and resets it. It then enters a while-loop that runs until the 
    environment is considered "done". Within the loop, a random action is sampled from the environment's action space.
    That action is executed and the resulting observation, reward, done signal, and debug information are collected.
    """

    # gym_csgo registers the envs (to gym.make(...))
    # Gym environments

    # Open new environment context (automatically closes env at end of scope)
    with gym.make('csgo_dm-v0') as env:
        # Reset the environment
        env.reset()
        # Env is not done yet
        done = False
        # Until the environment is done
        while not done:
            # Get random action from environment
            action = env.action_space.sample()
            # Execute the random action and collect observation
            obs, rew, done, info = env.step(action)

            print(
                f'Action: {action}, Observation: {obs}, Reward: {rew}, Done: {done}, Info: {info}'
            )


if __name__ == '__main__':
    main()
