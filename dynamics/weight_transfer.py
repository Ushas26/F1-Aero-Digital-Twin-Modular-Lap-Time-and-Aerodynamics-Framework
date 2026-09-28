def weight_transfer(
    mass,
    accel,
    cg_height,
    wheelbase
):

    return (
        mass
        *accel
        *cg_height
        /wheelbase
    )