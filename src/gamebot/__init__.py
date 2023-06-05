import universe  # register the universe environments
import gym


def main():
	"""
	Run the main function which creates an OpenAI gym environment for 'flashgames.NeonRace-v0' and
	configures it to run in a local docker container. The function then initiates the environment and
	gets a list of observations of its initial state. It runs a while loop which takes an action of
	pressing the 'ArrowUp' key, and gets the next set of observation, reward, and done status of the
	environment. The environment is then rendered and the loop continues until the environment is
	done. No parameters or return types.
	"""
    # You can run many environment in parallel
    env = gym.make('flashgames.NeonRace-v0')
    env.configure(remotes=1)  # automatically creates a local docker container
    # Initiate the environment and get list of observations of its initial state
    observation_n = env.reset()
    while True:
        action_n = [[('KeyEvent', 'ArrowUp', True)]
                    for ob in observation_n]  # your agent here
        observation_n, reward_n, done_n, info = env.step(
            action_n)  # Reinforcement Learning action by agent
        print("observation: ", observation_n)  # Observation of the environment
        # If the action had any postive impact +1/-1
        print("reward: ", reward_n)
        env.render()  # Run the agent on the environment


if __name__ == '__main__':
    main()
