CN LAB: 7 simplified programs + reusable templates

Install: pip install simpy
For each program: run server.py in one terminal, then client.py in another. Run simulation.py separately. Multi_Chat supports multiple client terminals. Stop servers with Ctrl+C.

Ports: Multi_Chat 5000, ARP 5001, GBN 5002, SR 5003, CSMA 5004, Packet_Routing 5005, Wireless 5006. Template uses 5010.

These are educational demonstrations, not complete real-world protocol implementations. The socket code and SimPy code are independent demonstrations of each concept, not a live integrated network simulator. GBN/SR model a fixed single lost frame; CSMA/Wireless simplify shared-channel access.
