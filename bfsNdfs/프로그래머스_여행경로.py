def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    
    routes = {}
    
    for ticket in tickets:
        if ticket[0] in routes:
            routes[ticket[0]].append(ticket[1])
        else:
            routes[ticket[0]] = [ticket[1]]
    


    stacks = ["ICN"]
    
    while stacks:
        top = stacks[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stacks.pop())
        else:
            stacks.append(routes[top].pop())
            
    answer.reverse()
    return answer
