from MultiTaxiLib.taxi_environment import TaxiEnv


def test__get_observation_space_list():
    taxi_env = TaxiEnv()
    obs_space_list = taxi_env._get_observation_space_list()
    assert obs_space_list == [7, 12, 1, 7, 12, 7, 12, 4]


def test_reset():
    obs_image = TaxiEnv(observation_type='image').reset()
    obs_symbolic = TaxiEnv().reset()
    assert obs_image['taxi_1'].shape == (5, 5, 3)
    assert obs_symbolic['taxi_1'].shape == (8,)
