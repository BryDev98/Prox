def start_i(username,userdata,isadmin):
    msg = 'Bienvenido al BOT PR_Finder V1 ๐ฐ\n'
    msg+= '๐ค Versiรณn : V1.7 | ๐พCode by : @ShiraDesigner\n\n'
    msg+= '๐ค USUARIO : @' + str(username)+'\n\n'
    msg+= '๐ IP : ' + str(userdata['ip'])+'\n'
    msg+= 'โ RANGO MINIMO : ' + str(userdata['rango_minimo'])+'\n'
    msg+= 'โ RANGO MAXIMO : ' + str(userdata['rango_maximo'])+'\n\n'
    msgAdmin = '๐ค [USUARIO]'
    if isadmin:
        msgAdmin = '๐ [PROPIETARIO]'
    msg+= msgAdmin + '\n'
    return msg
