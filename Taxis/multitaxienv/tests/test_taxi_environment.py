from Taxis.multitaxienv.taxi_environment import TaxiEnv


def test__get_observation_space_list():
    taxi_env = TaxiEnv()
    obs_space_list = taxi_env._get_observation_space_list()
    assert obs_space_list == [7, 12, 1, 7, 12, 7, 12, 4]
