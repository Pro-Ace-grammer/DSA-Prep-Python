def TOH(n, src, aux, dest):
    if n == 1:
        print(f'Move disk {n} from {src} -> {dest}')
        return
    
    TOH(n-1, src, dest, aux)
    print(f'Move disk {n} from {src} -> {dest}')
    TOH(n-1,aux, src, dest)

TOH(3,'A','B','C')