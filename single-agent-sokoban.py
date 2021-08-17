from griddly import GymWrapper, gd

if __name__ == '__main__':

    env = GymWrapper(
        yaml_file='sokoban.yaml',
        gdy_path='.',
        image_path='.',
        global_observer_type=gd.ObserverType.SPRITE_2D
    )
    env.reset()

    # Replace with your own control algorithm!
    for s in range(1000):
        obs, reward, done, info = env.step(env.action_space.sample())
        env.render()  # Renders the environment from the perspective of a single player

        env.render(observer='global')  # Renders the entire environment

        if done:
            env.reset()
