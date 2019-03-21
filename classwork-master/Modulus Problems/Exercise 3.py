frame_time = 3605
fire_chances = frame_time // 60
fire_time_1 = (frame_time // 60) * 60
fire_time_2 = (frame_time // 120) * 60
fire_time_3 = (frame_time // 180) * 60
fire_time_4 = (frame_time // 240) * 60
print(f'The laser fired {fire_chances} times in {frame_time} frames.')
print(f'The laser shot at {fire_time_1} frames, {fire_time_2} frames, {fire_time_3} frames and {fire_time_4} frames.')

# if frame_time % 60 == 0, this means that a shot has been fired since the game is being rendered at 60 frames per second, and the laser shoots once per second; once per 60 frames.