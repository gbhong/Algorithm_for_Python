def solution(bridge_length, weight, truck_weights):
    queue = [0]*(bridge_length-1)
    queue.append(truck_weights.pop(0))

    t = 1
    total_weight = sum(queue)
    while queue:
        total_weight -= queue.pop(0)
        if truck_weights:
            if total_weight+truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
        t += 1
    return t

print(solution(100, 100, [10]))