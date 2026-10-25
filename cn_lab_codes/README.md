# CN Lab: user-input edition

This edition is based on the original simple ZIP, not the later full-implementation project. It preserves the three-file-per-program layout and adds interactive prompts. Enter at a prompt to accept the displayed default. All servers run on localhost; launch the relevant server in one terminal, then the matching client in another. Stop servers with Ctrl+C. For multi-chat, open two or more client terminals. SimPy simulations run **separately** from the socket programs.

## Setup

```bash
python -m pip install -r requirements.txt
cd ARP
python server.py
# in a separate terminal in the same directory:
python client.py
# independently:
python simulation.py
```

Repeat for each program. Do not run all servers in the same terminal. Ports: Multi_Chat 5000, ARP 5001, GBN 5002, SR 5003, CSMA 5004, Packet_Routing 5005, Wireless 5006.

## Inputs and examples

| Folder | Socket client prompts | SimPy prompts / examples |
|---|---|---|
| Multi_Chat | username, repeated messages; `exit` to quit | client count=3, messages/client=3, interval=1 |
| ARP | repeat IP lookup, blank quits; try `192.168.1.2` | IP=`192.168.1.1`, delay=2 |
| GBN | frames=5, window=3, lost frame=2 (`-1` for none) | same + per-frame delay=1 |
| SR | frames=5, window=3, lost frame=2 (`-1` for none) | same + per-frame delay=1 |
| CSMA | message; open simultaneous clients for busy-channel example | stations=3, TX duration=2 |
| Packet_Routing | source=A, destination=D | source=A, destination=D |
| Wireless | device name, message count, messages | devices=3, packets/device=1, delay=2 |
| CSMA/CA alternate | no separate socket program; original alternate preserved | `simulation_csma_ca_user_input.py`: nodes=5, CW min=4, CW max=16, slot=.001, TX=.01, retries=4, duration=10, arrival=20 |

## Files

Each folder has `server.py`, `client.py`, `simulation.py`; CSMA additionally has the **unchanged** `simulation_csma_ca_alternate.py` and the new interactive `simulation_csma_ca_user_input.py`. `Templates/` contains the original three reusable templates. `README.txt` is preserved from the earlier ZIP.

## Scope / exam notes

GBN and SR remain educational request/response demonstrations with configurable frame count, window and one simulated loss; they do not implement a live timed sliding-window transport. ARP uses a server-side lookup table, not raw Ethernet ARP. CSMA uses a lock and the basic SimPy simulation uses a shared resource, not real collision detection. Wireless uses TCP sockets as an access-point analogy, not Wi-Fi hardware. The original CSMA/CA alternate model is preserved as supplied; its `busy` flag serializes simultaneous transmitters in SimPy and does not accurately count physical collisions. The new interactive version uses the same original model. Routing uses the example directed topology shown in `Packet_Routing/server.py` and `simulation.py`.
