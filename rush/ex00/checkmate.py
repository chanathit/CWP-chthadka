def checkmate(board):
    try:
        rows = board.split('\n')
        if rows and rows[-1] == "":
            rows.pop()
            
        if not rows:
            print("Error")
            return
            
        size = len(rows)
        for r in rows:
            if len(r) != size:
                print("Error")
                return
                
        kr, kc = -1, -1
        k_count = 0
        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    kr, kc = r, c
                    k_count += 1
                    
        if k_count != 1:
            print("Error")
            return
            
        PIECES = ['K', 'Q', 'B', 'R', 'P']
            
        def is_enemy(r, c, attackers):
            if 0 <= r < size and 0 <= c < size:
                char = rows[r][c]
                if char in attackers:
                    return True
                if char in PIECES: 
                    return "Blocked"
            return False

        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diagonals:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                res = is_enemy(r, c, ['B', 'Q'])
                if res is True:
                    print("Success")
                    return
                elif res == "Blocked":
                    break
                r += dr
                c += dc
                
        straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in straights:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                res = is_enemy(r, c, ['R', 'Q'])
                if res is True:
                    print("Success")
                    return
                elif res == "Blocked":
                    break
                r += dr
                c += dc
                
        if kr + 1 < size:
            if kc - 1 >= 0 and rows[kr+1][kc-1] == 'P':
                print("Success")
                return
            if kc + 1 < size and rows[kr+1][kc+1] == 'P':
                print("Success")
                return

        print("Fail")
        
    except Exception:
        print("Error")