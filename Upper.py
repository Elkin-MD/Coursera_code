while True:
    fname = input('Enter file name: ')
    if fname == 'done':
        print('See ya')
        break
    else:
        try:
            fo = open(fname)
            for line in fo:
                ys = line.rstrip()
                print(ys.upper())
        except:
            print('File could not be opened')