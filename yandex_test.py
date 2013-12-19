def checkEmail(string):
    '''
    (str -> str)

    Checks an e-mail inputed by user on several conditions:
    1. e-mail состоит из имени и доменной части, эти части разделяются символом "@";
    2. доменная часть не короче 3 символов и не длиннее 256, является набором непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой;
    3. каждый компонент доменной части не может начинаться или заканчиваться символом "-";
    4. имя (до @) не длиннее 128 символов, состоит из символов a-z0-9"._-;
    5. в имени не допускаются две точки подряд;
    6. если в имени есть двойные кавычки ", то они должны быть парными;
    7. в имени могут встречаться символы "!,:", но только между парными двойными кавычками.
    
    Prints out "Спасибо, Ваш e-mail принят." if input satisfies all the conditions. If not, prints out a message, asking to repeat their input and prints errors they made.
    '''
    allowed_symbols = 'qwertyuiopasdfghjklzxcvbnm1234567890"._-'
    allowed_symbols1 = 'qwertyuiopasdfghjklzxcvbnm1234567890"._-!,:'
    mistakes = 0
    s = string.lower()
    #check 1st condition
    if (not s.count('@') == 1) or len(s) < 4:
        print 'Проверьте ввод e-mail адреса! Он должен быть вида "example@yandex.ru"'
        return None

    #decompose e-mail in 2 parts: e-mail name and domain
    part1 = s[:s.find('@')]
    part2 = s[s.find('@')+1:]

    if not '.' in part2:
        print 'Проверьте ввод e-mail адреса! Он должен быть вида "example@yandex.ru"'
        return None

    #check 2nd condition
    if len(part2) < 3 or len(part1) > 256:
        print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
        print '-доменная часть (знаки после "@") должна быть не короче 3 символов и не длиннее 256'
        mistakes += 1
    for i in part2:
        if not i in allowed_symbols:
            if mistakes == 0:
                print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
                print '-доменная часть (знаки после "@") должна состоять из символов a-z 0-9._-'
            else:
                print '-доменная часть (знаки после "@") должна состоять из символов a-z 0-9._-'
            mistakes += 1
            break

    #check 3rd condition
    d = []
    def domainparts(part):
        while '.' in part:
            for i in part:
                if i == '.':
                    d.append(part[:part.find('.')])
                    return domainparts(part[part.find('.')+1:])
        d.append(part)
        return d
    dom_parts = domainparts(part2)   
    for i in dom_parts:
        if len(i) > 0 and (i[0] == '-' or i[-1] == '-'):
            if mistakes == 0:
                print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
                print '-каждая часть доменной части (разделенные точкой) не может начинаться или заканчиваться символом "-"'
            else:
                print '-каждая часть доменной части (разделенные точкой) не может начинаться или заканчиваться символом "-"'
            mistakes += 1
            break

    for i in dom_parts:
        if i == '':
            if mistakes == 0:
                print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
                print '-доменная часть (знаки после "@") не может начинаться или заканчиваться знаком "." и не может содержать больше одного знака "." подряд'
            else:
                print '-доменная часть (знаки после "@") не может начинаться или заканчиваться знаком "." и не может содержать больше одного знака "." подряд'
            mistakes += 1
            break

    #check 4th condition
    if len(part1) > 128:
        if mistakes == 0:
            print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
            print '-имя (знаки до "@") должно быть не длиннее 128 символов'
        else:
            print '-имя (знаки до "@") должно быть не длиннее 128 символов'
        mistakes += 1
    for i in part1:
        if not i in allowed_symbols1:
            if mistakes == 0:
                print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
                print '-имя (знаки до "@") должно состоять из символов a-z 0-9 "._-'
            else:
                print '-имя (знаки до "@") должно состоять из символов a-z 0-9 "._-'
            mistakes += 1
            break

    #check 5th condition
    if '..' in part1:
        if mistakes == 0:
            print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
            print '-в имени (знаки до "@") не может быть больше одного знака "." подряд'
        else:
            print '-в имени (знаки до "@") не может быть больше одного знака "." подряд'
        mistakes += 1

    #check 6th condition
    if not (part1.count('"') % 2 == 0):
        if mistakes == 0:
            print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
            print '-если в имени (знаки до "@") используются кавычки ("), то они должны быть парными'
        else:
            print '-если в имени (знаки до "@") используются кавычки ("), то они должны быть парными'
        mistakes += 1

    #check 7th condition
    f=[]
    def spec_symbols(string):
        c0 = 0
        c1 = 0
        while '!' in string or ',' in string or ':' in string:
            for i in string:
                c0 += 1
                if i == '!' or i == ',' or i == ':':
                    for j in string[c0-1:]:
                        c1 += 1
                        if j in allowed_symbols:
                            f.append(string[c0-2]+string[c0-1:][:c1])
                            return spec_symbols(string[string.find(i)+c1:])
        return f
    name_parts = spec_symbols(part1)
    for i in name_parts:
        if not (i[0] == '"' and i[-1] == '"'):
            if mistakes == 0:
                print 'E-mail адрес введён неправильно. Проверьте следующие требования к вводу e-mail:'
                print '-в имени (знаки до "@") могут встречаться символы "!,:", но только между парными двойными кавычками'
            else:
                print '-в имени (знаки до "@") могут встречаться символы "!,:", но только между парными двойными кавычками'
            mistakes += 1
    
    
    #final output
    if mistakes == 0:
        print 'Спасибо! Ваш e-mail был введён корректно и был принят системой.'
    else:
        print 'Повторно введите Ваш e-mail.'
