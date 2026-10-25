import simpy
import random

random.seed(10)

N = int(input("Number of nodes [5]: ") or 5)
CW_MIN = int(input("Minimum contention window [4]: ") or 4)
CW_MAX = int(input("Maximum contention window [16]: ") or 16)
SLOT = float(input("Slot duration [0.001]: ") or 0.001)
TX_TIME = float(input("Transmission duration [0.01]: ") or 0.01)
MAX_RETRIES = int(input("Max retries [4]: ") or 4)
SIM_TIME = float(input("Simulation time [10]: ") or 10)
ARRIVAL = float(input("Arrival rate per node [20]: ") or 20)
if not (N > 0 and 0 < CW_MIN <= CW_MAX and SLOT > 0 and TX_TIME > 0 and MAX_RETRIES >= 0 and SIM_TIME > 0 and ARRIVAL > 0):
    raise ValueError("Invalid simulation parameters")

def node(env, name, channel, stats):
    while True:
        yield env.timeout(random.expovariate(ARRIVAL))
        stats["generated"] += 1
        print(f"{env.now:.3f}: {name} packet generated")

        cw, retry = CW_MIN, 0

        while retry <= MAX_RETRIES:
            backoff = random.randrange(cw)
            print(f"{env.now:.3f}: {name} backoff = {backoff}")

            while backoff > 0:
                if channel["busy"]:
                    print(f"{env.now:.3f}: {name} channel busy - waiting")
                    yield env.timeout(SLOT)
                else:
                    print(f"{env.now:.3f}: {name} channel idle")
                    yield env.timeout(SLOT)
                    backoff -= 1

            if channel["busy"]:
                stats["collisions"] += 1
                retry += 1
                stats["retries"] += 1
                cw = min(cw * 2, CW_MAX)
                print(f"{env.now:.3f}: {name} collision - retry {retry}")
                continue

            channel["busy"] = True
            print(f"{env.now:.3f}: {name} channel busy - transmitting")
            yield env.timeout(TX_TIME)
            channel["busy"] = False
            stats["success"] += 1
            print(f"{env.now:.3f}: {name} transmission successful")
            break

        if retry > MAX_RETRIES:
            stats["dropped"] += 1
            print(f"{env.now:.3f}: {name} packet dropped")

env = simpy.Environment()
channel = {"busy": False}
stats = {
    "generated": 0, "success": 0,
    "collisions": 0, "retries": 0, "dropped": 0
}

for i in range(N):
    env.process(node(env, f"N{i+1}", channel, stats))

print("CSMA/CA Simulation Started")
env.run(until=SIM_TIME)

print("\n--- RESULTS ---")
for key, value in stats.items():
    print(key.capitalize(), ":", value)

g = stats["generated"]
print("Collision Rate:",
      round(stats["collisions"] / g * 100, 2) if g else 0, "%")
print("Retransmission Rate:",
      round(stats["retries"] / g * 100, 2) if g else 0, "%")
print("CSMA/CA Simulation Completed")
