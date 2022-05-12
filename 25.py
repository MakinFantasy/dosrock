for a in range(10):
    for b in range(10):
        x = int(f'12345{a}6{b}8')
        if x % 17 == 0:
            print(x, x // 17)