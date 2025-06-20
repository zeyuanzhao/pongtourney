import math

prev_ball_pos = [None, None]
ball_velocity = [0, 0]

def predict(paddle_frect, other_paddle_frect, ball_frect, table_size):
    [ball_x, ball_y] = get_point(ball_frect)
    [ball_speed_x, ball_speed_y] = ball_velocity
    [ball_size_x, ball_size_y] = get_size(ball_frect)
    [paddle_x, paddle_y] = get_point(paddle_frect)
    x_travel_distance = abs(paddle_x - ball_x) - paddle_frect.size[0]/2 - ball_size_x/2

    travel_time = x_travel_distance / abs(ball_speed_x)
    projected_y = ball_y + ball_speed_y * travel_time
    period = 2 * table_size[1]
    mod_y = projected_y % period
    return mod_y if mod_y <= table_size[1] else period - mod_y

    # x = 0
    # if ball_speed_y < 0:
    #     i = -1
    # else:
    #     i = 1
    # position = ball_y
    # while x<y_travel_distance:
    #     if ball_y + ball_size_y/2 >= table_size[1]-2 or ball_y - ball_size_y/2 <= 2: 
    #         return None
    #     elif ball_y + ball_size_y/2 + x >= table_size[1] or ball_y - ball_size_y/2 - x <= 0:
    #         y_travel_distance -= x
    #         i *= -1
    #         x = 0
    #         continue
    #     elif x%table_size[1] == 0 and x != 0:
    #         y_travel_distance -= x
    #         i *= -1
    #         x = 0
    #         continue
    #     x += 1
    # print(position + x * i)
    # return position + x * i
    
def get_point(element):
    return [element.pos[0] + element.size[0] / 2, element.pos[1] + element.size[1] / 2]

def get_size(element):
    return [element.size[0], element.size[1]]

def get_velocity_ball(ball_frect):
    global ball_velocity
    [prev_ball_x, prev_ball_y] = prev_ball_pos
    [ball_x, ball_y] = get_point(ball_frect)
    if prev_ball_x is None or prev_ball_y is None:
        ball_velocity = [0, 0]
    else:
        ball_velocity = [ball_x - prev_ball_x, ball_y - prev_ball_y]
    prev_ball_pos[0] = ball_x
    prev_ball_pos[1] = ball_y


def check_return(paddle_frect, table_size):
    if is_left(paddle_frect, table_size):
        if ball_velocity[0] < -0.1:
            return True
    else:
        if ball_velocity[0] > 0.1:
            return True
    return False

def is_left(paddle_frect, table_size):
    [paddle_x, paddle_y] = get_point(paddle_frect)
    return paddle_x < table_size[0] / 2
    
def ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    [paddle_x, paddle_y] = get_point(paddle_frect)
    [ball_x, ball_y] = get_point(ball_frect)
    [paddle_x_size, paddle_y_size] = get_size(paddle_frect)
    [other_paddle_x, other_paddle_y] = get_point(other_paddle_frect)
    ball_x = get_point(ball_frect)[0]
    ball_y = get_point(ball_frect)[1]
    get_velocity_ball(ball_frect)  # Update global ball_velocity once per frame
    # check_hit = (is_left(paddle_frect, table_size) and abs(ball_x - other_paddle_x - paddle_x_size / 2) < 10) or (not (is_left(paddle_frect, table_size)) and abs(ball_x - other_paddle_x + paddle_x_size / 2) < 10)
    if ball_x < 1 or ball_x > table_size[0] - 1 or ball_y < 1 or ball_y > table_size[1] - 1:
        return "None"         
    if check_return(paddle_frect, table_size):
        go_to = predict(paddle_frect, other_paddle_frect, ball_frect, table_size)
    else:
        go_to = table_size[1] / 2
    if go_to is None:
        return "none"
    if paddle_y + paddle_y_size / 5 < go_to:
        return "down"
    elif paddle_y - paddle_y_size / 5 > go_to:
        return "up"
    else:
        return "none"
