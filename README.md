# MullvadDNS Leak

Example Proof of Concept (POC) of the Mullvad Android DNS leak.

---

### Host Computer:

1: **Listen for Port 53 (DNS) on Device Host**

```sh
tcpdump -i br-lan udp and host <DEVICE-HOST> and port 53
```

---

### Android Device:

1: Import the WireGuard Configurations

- Import the WireGuard configurations from config/wg1.conf and config/wg2.conf.

2: Create a Constant Stream of Requests

#### constant stream of requests - Python

```
python request.py
```

#### constant stream of requests - HTML / Browser

- Open request.html in your selected browser.
  4: Trigger the Leak
- With your host computer listening for changes, open the WireGuard app on your Android device and switch between wg1.conf to wg2.conf.
