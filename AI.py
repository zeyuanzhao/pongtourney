import math

def predict(paddle_frect, other_paddle_frect, ball_frect, table_size):
    [ball_x, ball_y] = get_point(ball_frect)
    [ball_speed_x, ball_speed_y] = get_velocity_ball(ball_frect)
    [ball_size_x, ball_size_y] = get_size(ball_frect)
    [paddle_x, paddle_y] = get_point(paddle_frect)
    [other_paddle_x, other_paddle_y] = get_point(other_paddle_frect)
    # hit_angle = other_paddle_frect.get_angle(ball_y) 
    # slope = math.tan(hit_angle)
    # slope = ball_speed_y/ball_speed_x
    x_travel_distance = abs(paddle_x - other_paddle_x) - paddle_frect.size[0]
    travel_time = (x_travel_distance / abs(ball_speed_x))
    y_travel_distance = ball_speed_y * travel_time

    x = 0
    i = 1
    position = ball_y
    first_hit = True 
    while x<y_travel_distance:
        if (ball_y + ball_size_y/2 + x >= table_size[1] or ball_y - ball_size_y/2 - x <= 0) and first_hit:
            position += x * i
            first_hit = False
            i *= -1
            y_travel_distance -= x
            x = 0
        elif x%table_size[1] == 0:
            position += x * i
            i *= -1
            y_travel_distance -= x
            x = 0
        x += 1
    return position + x * i
    
def get_point(element):
    return [element.pos[0] + element.size[0] / 2, element.pos[1] + element.size[1] / 2]

def get_size(element):
    return [element.size[0], element.size[1]]

def get_velocity_ball(ball_frect):
    return [ball_frect.speed[0], ball_frect.speed[1]]

def get_speed_paddle(paddle_frect):
    return [paddle_frect.speed]

# def check_opponent_collision(ball_frect, other_paddle_frect):
#     [ball_x, ball_y] = get_point(ball_frect)
#     [ball_size_x, ball_size_y] = get_size(ball_frect)
#     [other_paddle_x, other_paddle_y] = get_point(other_paddle_frect)
#     [other_paddle_size_x, other_paddle_size_y] = get_size(other_paddle_frect)
#     if abs(ball_x - other_paddle_x) < ball_size_x/2 + other_paddle_size_x/2:
#         return True
#     return False

def check_return(paddle_frect, ball_frect, table_size):
    if is_left(paddle_frect, table_size):
        if get_velocity_ball(ball_frect)[0] < 0:
            return True
    else:
        if get_velocity_ball(ball_frect)[0] > 0:
            return True
    return False

def is_left(paddle_frect, table_size):
    [paddle_x, paddle_y] = get_point(paddle_frect)
    return paddle_x < table_size[0] / 2
    
def ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    paddle_y = get_point(paddle_frect)[1]
    if check_return(paddle_frect, ball_frect, table_size):
        go_to = predict(other_paddle_frect, ball_frect, table_size)
    else:
        go_to = table_size[1] / 2
    if paddle_y < go_to:
        return "up"
    else:
        return "down"
