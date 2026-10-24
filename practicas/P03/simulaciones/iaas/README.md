# Simulaciones de IaaS

Imágenes ilustrativas generadas con la herramienta integrada de imágenes, basadas en las referencias visuales de la terminal y Firefox. No se creó una VM, no se ejecutó una conexión SSH y no se verificó un servidor público. Las IP son ejemplos.

- [Configuración de VM y firewall](1-configuracion-vm.png)
- [Sesión SSH e instalación de Nginx](2-sesion-ssh.png)
- [Página Nginx en Firefox](3-nginx-firefox.png)

## Prompts de generación

### Imagen 1

Use case: ui-mockup. Create an educational SIMULATED screenshot of AWS EC2 VM configuration, using the provided image ONLY as reference for the macOS Firefox window chrome, dark purple browser theme and Spanish UI. Replace the GitHub webpage with a realistic dark AWS EC2 instance summary. Keep browser chrome but use a single EC2 tab, no unrelated tabs. Persistent clear visible badge at top of webpage: "SIMULACIÓN · Ejemplo ilustrativo". Show instance name "practica3-web", state "En ejecución", operating system "Ubuntu Server 24.04 LTS", instance type "t3.micro", region "México (Central)", example public IPv4 "203.0.113.10", private IPv4 "10.0.1.25", key pair "practica3", storage "8 GiB gp3". Show a security group section with two readable inbound rules: SSH / TCP / 22 / 198.51.100.25/32 (Mi IP de ejemplo), HTTP / TCP / 80 / 0.0.0.0/0. Small note "Direcciones IP de ejemplo; no son recursos desplegados." Do not claim guaranteed free tier eligibility or show real account IDs. Crisp readable Spanish labels, clean plausible console layout. Landscape 2048x1152.

### Imagen 2

Use case: ui-mockup. Create an educational simulated SSH terminal screenshot matching the provided macOS terminal style: dark navy background, retro monospaced font, amber commands and cyan accents, same macOS window title and red yellow green window buttons. Replace ALL terminal contents with the following concise coherent session. At the top INSIDE the terminal clearly display "SIMULACIÓN · Sesión SSH de ejemplo". Then show local command: chmod 400 ~/Downloads/practica3.pem ; on next command line ssh -i ~/Downloads/practica3.pem ubuntu@203.0.113.10. Then "Welcome to Ubuntu 24.04 LTS (GNU/Linux x86_64)" and "IPv4 address for eth0: 10.0.1.25". Remote prompt must be ubuntu@ip-10-0-1-25:~$ and show successive commands "sudo apt update", brief plausible successful package index output, "sudo apt install -y nginx", brief successful installation output, "sudo systemctl enable --now nginx", "systemctl is-active nginx", output "active", "curl -I http://localhost", output "HTTP/1.1 200 OK", "Server: nginx", "Content-Type: text/html". Finish at empty remote prompt. Keep terminal text fully readable and not too dense, no invented credentials, no long logs, no actual claims of a live machine. Bottom line "203.0.113.10 es una IP de documentación". Landscape 2048x1152.

### Imagen 3

Use case: ui-mockup. Create an educational simulated screenshot matching the reference macOS Firefox window, dark purple Firefox chrome, red yellow green window buttons, Spanish menu bar. Replace all GitHub content with a plain white default Nginx welcome page. Use one browser tab titled "Welcome to nginx!" and the address bar visibly reads "http://203.0.113.10" with a plain HTTP not-secure indicator (not a secure padlock). Near the top of the web content display a clearly visible modest banner "SIMULACIÓN · Vista de ejemplo, sin servidor desplegado". Below, reproduce the familiar minimalist nginx default welcome page: narrow centered column, large black heading "Welcome to nginx!", paragraph "If you see this page, the nginx web server is successfully installed and working. Further configuration is required.", paragraph "For online documentation and support please refer to nginx.org.", and italic "Thank you for using nginx." Bottom small line "IP de documentación: 203.0.113.10". No actual account details. Preserve overall Firefox appearance but omit unrelated tabs. Crisp typography. Landscape 2048x1152.

## Ajustes finales

Se simplificaron los logs de paquetes de la terminal para evitar versiones inconsistentes. Se corrigió la zona de disponibilidad a mx-central-1a y se agregó sudo al comando systemctl enable --now nginx. Se conservaron los rótulos de simulación.

