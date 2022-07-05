from spinup.utils import test_policy as tp


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    ## parser.add_argument('fpath', type=str)
    parser.add_argument('--len', '-l', type=int, default=0)
    parser.add_argument('--episodes', '-n', type=int, default=100)
    parser.add_argument('--norender', '-nr', action='store_true')
    parser.add_argument('--itr', '-i', type=int, default=-1)
    parser.add_argument('--deterministic', '-d', action='store_true')
    args = parser.parse_args() 
    
    env, get_action = tp.load_policy_and_env('GripperPegInHole2DPyBulletEnv-v1',
                                             args.itr if args.itr >=0
                                             else 'last',
                                             args.deterministic)
    tp.run_policy(env, get_action, args.len, args.episodes, not(args.norender))  
