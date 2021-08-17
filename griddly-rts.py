from griddly import GymWrapper, gd
from griddly.util.wrappers import ValidActionSpaceWrapper

if __name__ == '__main__':

    env = GymWrapper(
        yaml_file='griddly_rts.yaml',
        gdy_path='.',
        image_path='.',
        player_observer_type=gd.ObserverType.ISOMETRIC,
        global_observer_type=gd.ObserverType.ISOMETRIC
    )
    env.reset()

    # Only select valid actions
    env = ValidActionSpaceWrapper(env)

    # Replace with your own control algorithm!
    for s in range(1000):
        obs, reward, done, info = env.step(env.action_space.sample())
        for p in range(env.player_count):
            env.render(observer=p)  # Renders the environment from the perspective of a single player

        env.render(observer='global')  # Renders the entire environment

        if done:
            env.reset()
