from dodal.beamlines import i20_1

device = i20_1.device(fake_with_ophyd_sim=True)


def test_direct_movement():
    test_sim_device = OphydDevice()
    result = await  i20_1_bluesky.direct_movement(test_sim_device)

