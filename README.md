# Personal Hosts
![Latest Release](https://img.shields.io/badge/Latest%20Release-0.2-blue?style=for-the-badge) ![Latest Release](https://img.shields.io/badge/Last%20Update-4th%20July%2C%202022-yellowgreen?style=for-the-badge)


This project contains the different variations of Host files used to block domains. The files can be used across Windows, Android, Pi Hole, etc. There are a few variations of the files for different use cases.

The source of the project is the ever expanding and mighty useful [Steven Black Hosts](https://github.com/StevenBlack/hosts)

Uses **v 3.10.13** of Steven Black Hosts.

[![Latest Release](https://img.shields.io/github/release/StevenBlack/hosts.svg?style=flat-square)](https://github.com/StevenBlack/hosts/releases) [![Last Commit](https://img.shields.io/github/last-commit/StevenBlack/hosts.svg?style=flat-square)](https://github.com/StevenBlack/hosts/commits/master) [![Commits Since](https://img.shields.io/github/commits-since/StevenBlack/hosts/latest.svg?style=flat-square)](https://github.com/StevenBlack/hosts/commits/master)

This project uses the default **Unified Hosts + Social list** and modifying it.

## Basic Information

1. The default hosts file will block all services in Desktop and Mobile. This includes - all social media, Gmail, Reddit, Google Play services, Pinterest, etc. 
***(It is not recommended to use this file)***
2. The hosts file in the Desktop and Mobile folder will block all services across social media and ads with some specific adjustments.

### Desktop
| **Allows**  | **Blocks**     |
|-------------|----------------|
| Reddit      | Adobe          |
| Tumblr      | Luminar        |
| Pinterest   | Edge Telemetry |
| Google Play |                |

### Mobile
1. Default hosts file blocks all - ad + social media + Google Play Services. 
***(Blocking Google Services will create issues on the working of Play Store, Maps, Backups, etc.)***
2. `HOSTS_2` allows the following - 
	* Reddit
	* Pinterest
	* Tumblr
	* Google Services
3. `HOSTS_3` allows in addition to `HOSTS_2`, the following - 
	* WhatsApp
4. `HOSTS_3_1` allows in addition to `HOSTS_3`, the following *(has WhatsApp)* - 
	* Instagram
5. `HOSTS_4` allows in addition to `HOSTS_2`, the following *(no WhatsApp)* - 
	* Instagram
6. `HOSTS_5` allows in addition to `HOSTS_2`, the following *(no WhatsApp)* - 
	* Twitter
7. `HOSTS_5_1` allows in addition to `HOSTS_3`, the following *(has WhatsApp)* - 
	* Twitter

