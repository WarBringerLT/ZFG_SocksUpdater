from os import system, path, chdir
from sys import argv
if len(path.dirname(argv[0])) != 0: chdir(path.dirname(argv[0])) # Set Working Dir to Script Location


servers_file = open('API_ALIVE_SOCKS4.list','r')
servers_list = servers_file.readlines()
servers_file.close()

Proxy_max = 200
Host_IP = '127.0.0.1'
HOST_PORT = '3128' # Host Port
Added_Proxies = 0

pproxy_server_args = f"pproxy -l socks4+socks5://{Host_IP}:{HOST_PORT} "
for server in servers_list:
	if Added_Proxies < Proxy_max:
		server = server.strip()
		pproxy_server_args += f"-r socks4+socks5://{server} "
		Added_Proxies += 1

pproxy_server_args += "-s rr " # add Round-robin method
pproxy_server_args += '-v'     # add Verbose
#print(f"[!] PProxy-server-args: {pproxy_server_args}")
print('\n'*50)
print(f"[!] Total Proxy Servers Available: {len(servers_list)}")
print(f"[!] Total Proxy Servers Selected for Use: {Proxy_max}")
print("[!] Starting PProxy Engine...")
try:
	system(pproxy_server_args) # Launch PProxy Server
except KeyboardInterrupt:
	print(f"[!] PProxy server has been shut down! [KeyboardInterrupt]\n\n")


