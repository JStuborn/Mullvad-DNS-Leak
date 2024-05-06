# MullvadDNS Leak

Example Proof of Concept (POC) of the Mullvad Android DNS leak.
The challenge stems from an inherent flaw within the Android operating system, making it impossible to resolve without a patch from Android's developers. 
One workaround is to manipulate DNS settings temporarily while transitioning between configurations.

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

### View DNS Changes
Since `Block connections without VPN” was active`, nothing except encrypted WireGuard traffic should have left the device, but here we see plaintext DNS leaving the device.
```
11:50:27.816359 IP Pixel-Tablet.lan.53353 > OpenWrt.lan.53: 11200+ A? 307lf5rgn6-19282-11-50-27-519z.mullvad.test.lan. (65)
11:50:27.816359 IP Pixel-Tablet.lan.48267 > OpenWrt.lan.53: 44347+ A? 307lf5rgn6-19284-11-50-27-579z.mullvad.test.lan. (65)
11:50:27.816396 IP Pixel-Tablet.lan.16747 > OpenWrt.lan.53: 44584+ A? 307lf5rgn6-19289-11-50-27-729z.mullvad.test. (61)
11:50:27.816458 IP OpenWrt.lan.53 > Pixel-Tablet.lan.53353: 11200 NXDomain 0/0/0 (65)
11:50:27.816476 IP Pixel-Tablet.lan.45727 > OpenWrt.lan.53: 40503+ A? 307lf5rgn6-19290-11-50-27-759z.mullvad.test. (61)
11:50:27.816542 IP OpenWrt.lan.53 > Pixel-Tablet.lan.48267: 44347 NXDomain 0/0/0 (65)
11:50:27.816588 IP Pixel-Tablet.lan.43821 > OpenWrt.lan.53: 36295+ A? 307lf5rgn6-19291-11-50-27-789z.mullvad.test. (61) 
11:50:27.816625 IP OpenWrt.lan.53 > Pixel-Tablet.lan.16747: 44584 NXDomain 0/0/0 (61)
```
