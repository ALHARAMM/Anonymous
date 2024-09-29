import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 Anonymous.py')
    run('mkdir /usr/share/Anonymous')
    run('cp Anonymous.py /usr/share/Anonymous/Anonymous.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Anonymous/Anonymous.py "$@"')
    with open('/usr/bin/Anonymous','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/Anonymous & chmod +x /usr/share/Anonymous/Anonymous.py')
    print('''\n[*] Congratulation Anonymous is installed successfully...\n                                     
                                    AA
                                   AAA
                                  AAA
                                 AAA AAA
                                AAA  AAAA
                               AAA  AAAAAA
                              AAA  AAA  AAA
                             AAA  AAA    AAA
                            AAA  AAA      AAA
                           AAAAAAAAAAAAAAAAAAA
                               AAAA
                              AAAA
                             AAAA
          \nfrom now just type \x1b[6;30;42mAnonymous\x1b[0m in terminal ''')

if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/Anonymous ')
    run('rm /usr/bin/Anonymous ')
    print('[!] Now Anonymous Has Been Removed Successfully...')
