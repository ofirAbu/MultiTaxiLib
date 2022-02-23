from MultiTaxiLib.taxi_environment import TaxiEnv
from MultiTaxiLib.taxi_utils.rendering_utils import map2rgb, get_current_map_with_agents


def test__get_observation_space_list():
    taxi_env = TaxiEnv()
    obs_space_list = taxi_env._get_observation_space_list()
    assert obs_space_list == [7, 12, 1, 7, 12, 7, 12, 4]


def test_reset():
    obs_image = TaxiEnv(observation_type='image').reset()
    obs_symbolic = TaxiEnv().reset()
    assert obs_image['taxi_1'].shape == (5, 5, 3)
    assert obs_symbolic['taxi_1'].shape == (8,)


def test_map2rgb_fuel_station_bag():
    taxi_env = TaxiEnv(observation_type='image')
    orig_map = taxi_env.desc
    rgb_arr = map2rgb(taxi_env.state, orig_map)
    for station_coord in taxi_env.fuel_stations:
        assert all(rgb_arr[station_coord[0] + 1, station_coord[1] * 2 + 1] != rgb_arr[0, 0])
