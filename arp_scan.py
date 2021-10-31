import nmap, re, traceback
from typing import Pattern, Match




class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"
###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset







def arp_scan():
    ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    # Ask user to input the ip address they want to scan.
    while True:
        print(f"**{yellow}**Enter the IP address for scanning  {reset}\n ")
        ip_add_entered = input('** ')
        #sip_add_entered = ip_add_pattern.search(ip_add_entered)
        if ip_add_pattern:
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print(f"**{yellow}**Enter the port range {reset}\n ")
        global port_range, master_results
        port_range = input("* ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        print(type(port_range_valid))
        print(f'{yellow}The Ports Entered.. {reset}\n{port_range_valid}')
       # port_range_valid = str(port_range_valid)


        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            print(f'{yellow}[PORT-MIN]-- {reset}[{port_min}]\n{yellow}[PORT-MAX]{reset}{port_max}')
            break


    try:
        master_results = []
        print()
        print('X'*50)
        print(f'{yellow}**Parsing First Run.{reset}')
        nm = nmap.PortScanner()
        ip_add_entered=str(ip_add_entered)
        host = ip_add_entered + '/24'
        nm.scan(hosts=host, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print(f'{yellow} :: [HOST-Status] {reset}')
            print(f"{host} :: {status}")
            nm.scan(ip_add_entered, port_range)

            for host in nm.all_hosts():
                print('----------------------------------------------------')
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('----------')
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    lport.sort()
                    for port in lport:
                        print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    except:
        print('Error in running all_host arg')


        # protocol
    try:
        protocols = nm[ip_add_entered].all_protocols()

        print(f'{yellow}**[STATUS]{reset}\n{protocols}')
        master_results.append(protocols)

    except Exception as EA:
        print(f'{red}Error In Parsing PROTOCOL{reset}')
        print(EA)

        ## PROTOCOL
        try:
            status = nm[ip_add_entered].state()
            print(f'{yellow}**[PROTOCOL]{reset}\n{status}')
            master_results.append(status)
        except:
            print(f'{red}Error In Parsing status{reset}')

        ### HAS TCP
        try:
            has_tcp = nm[ip_add_entered]['tcp'].keys()
            print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
            master_results.append(has_tcp)

            port_22 = nm[ip_add_entered].has_tcp(22)
            print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
            master_results.append(port_22)
            if port_22 is True:
                info_22 = nm[ip_add_entered]['tcp'][22]
                print(f'{yellow}**[{info_22}]')
                master_results.append(info_22)
        except Exception as e:
            print(f'{red}ERROR IN TCP PARSE{reset}')
            print(e)

        ### HAS PORT 22

        ### HAS PORT 80
        try:
            port_80 = nm[ip_add_entered].has_tcp(80)
            print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
            master_results.append(port_80)
            if port_80 is True:
                info_80 = nm[ip_add_entered]['tcp'][80]
                print(f'{yellow}**[{info_80}]')
                master_results.append(info_80)

            ### HAS PORT 81
            port_81 = nm[ip_add_entered].has_tcp(81)
            print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
            master_results.append(port_81)
            if port_81 is True:
                info_81 = nm[ip_add_entered]['tcp'][81]
                print(f'{yellow}**[{info_81}]')
                master_results.append(info_81)

        except:
            print(f'{red}ERROR IN TCP PARSE{reset}')

    except KeyError as exkey:
        traceback.print_exc()
        print("[!] Cannot scan host!: " , exkey)

    for port in range(port_min, port_max + 1):
        try:
            print('X'*50)
            #port_max += 1
            ip_add_entered = str(ip_add_entered)
            port = str(port)
            result = nm.scan(ip_add_entered, str(port))
            print(f'**{yellow}All Dictinary Keys:: {reset} \n{[*result.values()]}') ## unpacks all dictinary keys
            print(result.keys())
            print('X'*50)
            print(f'{yellow}**[TARGET]-- {reset}[{ip_add_entered}]\n{yellow}*[PORT-MIN]{reset}{port_min} \n{yellow}*[PORT-MAX]{reset}{port_max}')
            print('X'*50)

            print(f'{yellow}**[RESULTS]{reset}')
            print(result)
            #print([(k, result[timestr]) for k in result])
            #print(f'{yellow}**[CURRENT-PORT]{reset}\n{result["scaninfo"]}')
            print(f'{yellow}**[CURRENT-PORT]{reset}\n{port}')

            ## basic scan info
            basic_info = nm.scaninfo()
            print(f'{yellow}**[BASIC-INFO]{reset}\n{basic_info}')

            ### ALL HOSTS
            all_hosts = nm.all_hosts()
            print(f'{yellow}**[ALL-HOSTS]{reset}\n{all_hosts}')


            print(f'{yellow}**[ELAPSED-TIME]{reset}\n{port}')
            print('X'*50)
            print(list(result.values()))
            master_results.append(result)

            try:
                has_tcp = nm[ip_add_entered]['tcp'].keys()
                print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
                master_results.append(has_tcp)

                port_22 = nm[ip_add_entered].has_tcp(22)
                print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
                master_results.append(port_22)
                if port_22 is True:
                    info_22 = nm[ip_add_entered]['tcp'][22]
                    print(f'{yellow}**[{info_22}]')
                    master_results.append(info_22)
            except Exception as e:
                print(f'{red}ERROR IN TCP PARSE{reset}')
                print(e)

                ### HAS PORT 22

                ### HAS PORT 80
            try:
                port_80 = nm[ip_add_entered].has_tcp(80)
                print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
                master_results.append(port_80)
                if port_80 is True:
                    info_80 = nm[ip_add_entered]['tcp'][80]
                    print(f'{yellow}**[{info_80}]')
                    master_results.append(info_80)

                ### HAS PORT 81
                port_81 = nm[ip_add_entered].has_tcp(81)
                print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
                master_results.append(port_81)
                if port_81 is True:
                    info_81 = nm[ip_add_entered]['tcp'][81]
                    print(f'{yellow}**[{info_81}]')
                    master_results.append(info_81)

            except:
                print(f'{red}ERROR IN TCP PARSE{reset}')

            ### end of scan
            if port == port_max:
                print(nm.csv())
                return f'{red}**End of arp scan {master_results}'


        except Exception as e:
            traceback.print_exc()
            print(f"{red}**ERROR IN NMAP SCAN[{port}]{reset}.\n[{e}]")



results = arp_scan()
print('X' * 50)
print(f'{yellow} ARP-SCAN COMPLETE')
print(results)
