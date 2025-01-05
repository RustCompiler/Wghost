import json,re,requests,datetime,shutil,time,urllib3
from platform import uname
from os import mkdir as MakeDirectory,system as SysCommand,remove
from bs4 import BeautifulSoup

BANNER = """
██╗    ██╗ ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██║    ██║██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║ █╗ ██║██║  ███╗███████║██║   ██║███████╗   ██║   
██║███╗██║██║   ██║██╔══██║██║   ██║╚════██║   ██║   
╚███╔███╔╝╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
                 Version : 1.0.0
               Developer : Rust-C
            Telegram : t.me/Rustseller
\n\n 
"""

try:

    def echo(data):
        print(data)

    def ClearTerminal():
        sys_device = uname()[0]
        if (sys_device == "Windows"):SysCommand("cls")
        else:SysCommand("clear");echo("\n[!] - Warning\n- This Program Work Only In (Windows 64BT)");pass

    ClearTerminal()


    def InputUser():
        echo(BANNER)
        text_input = '[+] Enter Host ( Without HTTP/HTTPS ) : '
        IO_HOST = str(input(text_input))
        rules = r"^[\d.]+$"
        if (len(IO_HOST) > 15):ClearTerminal();echo("\n\n[!] Warning\n- You do not have the right to enter data up to 56 bytes");exit()
        else:pass
        if re.match(rules, IO_HOST):pass
        else:ClearTerminal();echo("\n\n[!] Warning\n- You are only allowed to enter the IP address");exit()
        return IO_HOST

    def MemoryWebView(UWD):
        # UWD: UrlWeb Data 
        try:MAKE_CACHE = MakeDirectory("Cache")
        except FileExistsError:pass
        CREATE_INDEXFILE = open('Cache\\index.html','w',encoding='utf-8')
        Web_data = CREATE_INDEXFILE.write(UWD)
        CREATE_INDEXFILE.close()

    def ImportContent():
        try:RH_data = open('Cache\\index.html','r',encoding='utf-8');IMemorey = str(RH_data.read())
        except FileNotFoundError:pass
        return IMemorey
        
    def ProxyUsing():
        try:
            LOAD_PROXY = open('config\\proxy.json','r',encoding='utf-8')
            USE_DATA = json.loads(LOAD_PROXY.read())
            OPT_PROXY = USE_DATA['Use']
            if (OPT_PROXY == True):SET_IP = USE_DATA["Proxy"];return SET_IP
            elif (OPT_PROXY == False):return "IS_NOT"
            else:return "IS_NOT"
        
        except FileNotFoundError:
            return "IS_NOT"
        
        except json.JSONDecodeError:
            return "IS_NOT"
            

    def ProgramRust():    
        class Proccess:
            def __init__(self):
                try:
                    # Create Requests 
                    self.GET_DATA = str(InputUser())
                    self.return_proxy = ProxyUsing()
                    
                    if (self.return_proxy == "IS_NOT"):
                        self.GET_INFO = requests.get("https://scamalytics.com/ip/"+self.GET_DATA).content
                    
                    else:
                        self.SET_PROXY = {"http":self.return_proxy,"https":self.return_proxy}
                        self.GET_INFO = requests.get("https://scamalytics.com/ip/"+self.GET_DATA,proxies=self.SET_PROXY).content
                    
                    MemoryWebView(str(self.GET_INFO.decode()))
                    self.WEB_CONTENT = ImportContent()
                    self.load_html_content = BeautifulSoup(self.WEB_CONTENT, 'html.parser')
                    export = self.load_html_content.find_all('table')[0]
                    self.score_table = self.load_html_content.find_all('pre')[0]
                    self.PreSorter = BeautifulSoup(str(self.score_table),'html.parser')
                    self.BypassSWD  = BeautifulSoup(str(export),'html.parser')
                    # bypass string web data
               
                except IndexError:
                    ClearTerminal()
                    echo("\n\n[!] - Warning\n\n- HOST Not Found");exit()

                except requests.exceptions.ConnectionError:
                    ClearTerminal()
                    echo("\n\n[!] Warning\n- Internet Connection Error");exit()
                
                except requests.exceptions.Timeout:
                    ClearTerminal()
                    echo("\n\n[!] Warning\n- Timeout Request");exit()
               
                except requests.exceptions.ProxyError:
                    ClearTerminal()
                    echo("\n\n[!] Warning\n- Proxy Is Not Valid\n- Enter Proxy With (http/https)\n- For Example : http://192.168.100.100:80");exit()
               
                except urllib3.exceptions.LocationParseError:
                    echo("\n\n[!] Warning\n- Proxy Is Not Valid\n- Enter Proxy With (http/https)\n- For Example : http://192.168.100.100:80");exit()

                              
                self.reg_string = ['','[+] DataCenter : ']
                self.EXPORT_DATA = self.BypassSWD.get_text().replace('\n','')
                self.data_oprator = self.EXPORT_DATA.replace('Operator','\n[+] Result Status (PROXY/DNS/IP) \n\n')
                self.data_Hostname = self.data_oprator.replace('Hostname','\n[+] HostName : ')
                self.data_ASN = self.data_Hostname.replace('ASN','\n[+] ASN : ')
                self.Organization = self.data_ASN.replace('ISP Name','\n[+] ISP (INTERNET CENTER) : ')
                self.Location = self.Organization.replace('Organization Name','\n[+] Organization : ')
                self.country_name = self.Location.replace('Country Name','\n[+] Region : ')
                self.country_code = self.country_name.replace('Country Code','\n[+] Region Code : ')
                self.sate_province = self.country_code.replace('State / Province','\n[+] State / Province : ')
                self.district = self.sate_province.replace('District / County','\n[+] District / Country : ')
                self.city = self.district.replace('City','\n[+] City : ')
                self.postal_code = self.city.replace('Postal Code','\n[+] Postal Code : ')
                self.latitude = self.postal_code.replace('Latitude','\n[+] Latitude : ')
                self.longitude = self.latitude.replace('Longitude','\n[+] Longitude : ')
                self.datacenter = self.longitude.replace('Datacenter','Datacenter')
                self.bypass_text0x1 = self.datacenter.replace('Does the connecting device reside in a datacenter?','\n')
                self.VPN = self.bypass_text0x1.replace('VPN','\n[+] Is Virtual Private Network : ')
                self.Anonymizing = self.VPN.replace('Anonymizing','')
                self.tor = self.Anonymizing.replace('Tor Exit Node','\n[+] Is Tor : ')
                self.server = self.tor.replace('Server','\n[+] Is Server : ')
                self.public_proxy = self.server.replace('Public Proxy','\n[+] Is Public : ')
                self.web_proxy = self.public_proxy.replace('Web Proxy','\n[+] Is WebProxy : ')
                self.search_engine = self.web_proxy.replace('Search Engine Robot','\n[+] Bot Activity : ')
                self.domain_name = self.search_engine.replace('Domain Names','\n[+] Domian Name Server : ')
                self.bypass_text0x2 = self.domain_name.replace('Proxies','\n')
                self.bypass_text0x3 = self.bypass_text0x2.replace('Location','')
                self.connection_type = self.bypass_text0x3.replace('Connection type','\n[+] Connection TYPE : ')
                
                def replace_nth_match(match, replacements):return replacements.pop(0)
                self.OUT = re.sub(r'Datacenter', lambda match: replace_nth_match(match, self.reg_string), self.connection_type, count=2).replace('\n\n','')
                
                def JSONDECRYPTION():
                    global SCORE_DATA
                    SCORE_DATA = self.PreSorter.get_text()
                    SCORE = "\n[+] SCORE : "+str(json.loads(SCORE_DATA)['score'])
                    IP = "\n[+] DNS/PROXY/IP : "+str(json.loads(SCORE_DATA)['ip'])
                    RISK = "\n[+] RISK IN REAL INTERNET : "+str(json.loads(SCORE_DATA)['risk'])
                
                    
                    return IP,SCORE,RISK

                self.SHOW_DETAIL1 = JSONDECRYPTION()[0]
                self.SHOW_DETAIL2 = JSONDECRYPTION()[1]
                self.SHOW_DETAIL3 = JSONDECRYPTION()[2]
                print(self.SHOW_DETAIL1,self.SHOW_DETAIL2,self.SHOW_DETAIL3,"\n\n------------------------\n\n",self.OUT)
                
                def CreateLog(data):
                    try:MakeDirectory("Result-IP")
                    except FileExistsError:pass
                    LOG_NAME = str('Result-IP\\IP-'+str(json.loads(SCORE_DATA)['ip'])+'- ['+str(datetime.datetime.now()).replace(':','-')+']'+'.txt')

                    LOG_FILE = open(file=LOG_NAME,mode='w',encoding='utf-8')
                    LOG_WRITE = LOG_FILE.write(data)
                    LOG_FILE.close()

                self.SAVE_LOG = str(self.SHOW_DETAIL1+self.SHOW_DETAIL2+self.SHOW_DETAIL3+"\n\n------------------------\n\n"+self.OUT)
                CreateLog(self.SAVE_LOG)

                echo("\n\n[+] - SAVE LOG > Result-IP Directory\n")
                
                

        Proccess()

        def RemoveCache(dir):
            try:REMOVE_CACHEFILE = shutil.rmtree(dir)
            except FileNotFoundError:pass

        RemoveCache('./Cache')

    if (__name__ == "__main__"):
        ProgramRust()
        time.sleep(10)
        exit()

except KeyboardInterrupt:
    ClearTerminal()
    echo("\n\n[x] Warning\n\n- Exit Program And Free Memorey Data!")
