def is_solved(target,state):
        return target in state

def get_neighbours(state,jug1,jug2):
        jug1_to_jug2 = min(state[0], jug2 - state[1])
        jug2_to_jug1 = min(state[1], jug1 - state[0])
        return [
                ((jug1, state[1]), f'Napełnij J{jug1}'),
                ((state[0], jug2), f'Napełnij J{jug2}'),
                ((0, state[1]), f'Opróżnij J{jug1}'),
                ((state[0], 0), f'Opróźnij J{jug2}'),
                ((state[0] - jug1_to_jug2, state[1] + jug1_to_jug2),f'Przelej J{jug1} do J{jug2}'),
                ((state[0] + jug2_to_jug1, state[1] - jug2_to_jug1),f'Przelej J{jug2} do J{jug1}')
        ]

def water_jugs(jug1,jug2,target):
    jug1, jug2 = min(jug1, jug2), max(jug1, jug2)
    state = (0, 0)
    q = [state]
    visited = {state}
    prev = {state: None}
    action = {} 

    while len(q) > 0:
            current_state = q.pop(0)
            if is_solved(target,current_state):
                    break

            for neighbor, action_description in get_neighbours(current_state,jug1,jug2):
                    if neighbor not in visited:
                            prev[neighbor] = current_state
                            action[neighbor] = action_description
                            visited.add(neighbor)
                            q.append(neighbor)

    if not is_solved(target,current_state):
            print('Brak możliwości rozwiązania!')
    else:
            statement = []
            while prev[current_state] is not None:
                    statement.insert(0, f"{action[current_state]}  --->  {current_state}")
                    current_state = prev[current_state]
            
            statement.insert(0, f"Początkowo mamy  --->   (0,0)")
            print('\n'.join(statement))


# water_jugs(3,4,2)
water_jugs(3,5,6)