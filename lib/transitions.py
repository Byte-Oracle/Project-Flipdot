from transitions import edge_to_edge, lines
import random
def get_rand_transition():
    rand = random.randint(0, 1)
    match rand:
        case 0:
            return edge_to_edge
        case 1:
            return lines