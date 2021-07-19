def studentdata(sid,**arg):
    print('student id:{sid}')
    if 'name' or 'sclass' in arg:
        print('student name:{arg[name]}')
        print('student class:{arg[sclass]}')
        
studentdata(sid="s101",name="kowsi",sclass="VI")
