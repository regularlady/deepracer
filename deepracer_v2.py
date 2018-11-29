def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    '''
    @on_track (boolean) :: The vehicle is off-track if the front of the vehicle is outside of the white
    lines

    @x (float range: [0, 1]) :: Fraction of where the car is along the x-axis. 1 indicates
    max 'x' value in the coordinate system.

    @y (float range: [0, 1]) :: Fraction of where the car is along the y-axis. 1 indicates
    max 'y' value in the coordinate system.

    @distance_from_center (float [0, track_width/2]) :: Displacement from the center line of the track
    as defined by way points

    @car_orientation (float: [-3.14, 3.14]) :: yaw of the car with respect to the car's x-axis in
    radians

    @progress (float: [0,1]) :: % of track complete

    @steps (int) :: numbers of steps completed

    @throttle :: (float) 0 to 1 (0 indicates stop, 1 max throttle)

    @steering :: (float) -1 to 1 (-1 is right, 1 is left)

    @track_width (float) :: width of the track (> 0)

    @waypoints (ordered list) :: list of waypoint in order; each waypoint is a set of coordinates
    (x,y,yaw) that define a turning point

    @closest_waypoint (int) :: index of the closest waypoint (0-indexed) given the car's x,y
    position as measured by the eucliedean distance

    @@output: @reward (float [-1e5, 1e5])
    '''

    import math

    reward = 1e-3

    # Stay on the track!

    if not on_track:
        reward = -1
    elif progress == 1:
        reward = 1e-3
    else:
        reward = reward * progress

    # Keep the car tight to the centerline

    if distance_from_center >= 0.0 and distance_from_center <= 0.03:
        reward = 1.0

    # Need for Speed!
    if throttle < 0.5:
        reward *= 1 - (0.5 * throttle)

    # Please keep the steering controlled, reduce reward for wild steering
    if abs(steering) > .75:
        reward *= 0.75

    # add throttle penalty
    if throttle < 0.5:
        reward *= 0.80

    return float(reward)
