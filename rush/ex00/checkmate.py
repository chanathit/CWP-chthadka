def checkmate(board):
    # 1. เช็กกระดานว่าง
    if not board:
        print("Error")
        return

    # 2. แยกบรรทัดแบบเบสิก
    rows = []
    for r in board.split('\n'):
        if r != "":
            rows.append(r)
            
    if len(rows) == 0:
        print("Error")
        return
        
    size = len(rows)
    
    # 3. เช็กว่ากระดานเป็นสี่เหลี่ยมจัตุรัส
    for r in rows:
        if len(r) != size:
            print("Error")
            return
            
    # 4. หาตำแหน่ง King
    king_r = -1
    king_c = -1
    king_count = 0
    
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_r = r
                king_c = c
                king_count += 1
                
    if king_count != 1:
        print("Error")
        return
        
    pieces = ['K', 'Q', 'B', 'R', 'P']

    # --- ฟังก์ชันช่วยเดินหาศัตรู ---
    def scan_direction(dr, dc, enemies):
        r = king_r + dr
        c = king_c + dc
        while 0 <= r < size and 0 <= c < size:
            char = rows[r][c]
            if char in enemies:
                return True
            if char in pieces:
                return False
            r += dr
            c += dc
        return False
    # --------------------------

    # 5. เช็กแนวทแยง (เรียกใช้ฟังก์ชันย่อย)
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonals:
        if scan_direction(dr, dc, ['B', 'Q']):
            print("Success")
            return
            
    # 6. เช็กแนวตรง (เรียกใช้ฟังก์ชันย่อย)
    straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straights:
        if scan_direction(dr, dc, ['R', 'Q']):
            print("Success")
            return
            
    # 7. เช็กเบี้ย (Pawn)
    if king_r + 1 < size:
        if king_c - 1 >= 0 and rows[king_r + 1][king_c - 1] == 'P':
            print("Success")
            return
        if king_c + 1 < size and rows[king_r + 1][king_c + 1] == 'P':
            print("Success")
            return

    print("Fail")