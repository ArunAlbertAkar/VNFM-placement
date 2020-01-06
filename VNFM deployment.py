 /* VNF service initiation on OpenStack */
 config system global :: = {
     “set hostname”: “nfv_vnf”
 end
 }
   config system interface :: = {
                   “edit”: “port 2”
           “set mode”: “dhcp”
           “set alias”: “public”
           “set mtu-override”: “enable”
           “set mtu”: “1200”
  }
   next {
           “edit”: “port 3”
           “set mode”: “dhcp”
           “set alias”: “private”
           “set mtu-override”: “enable”
           “set mtu”: “1200”
    }
/* Initializing DHCP relay configuration for ZTMP */
 option space NEW_op;
 option NEW_op.config-file-name “ztp.sh”; 
 subnet 10.201.0.0 netmask 255.255.192.0
     {
        Host zta
          {
              Option host-name zta;
               Hardware Ethernet 00:a0:a5:81:79:72;       // Device MAC address
 Option tftp-server-name “10.201.11.153”;
 Option NEW_op. Transfer-mode “tftp”;
 Fixed-address 10.201.1.252;
             }
     }

