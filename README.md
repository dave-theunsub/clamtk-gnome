This readme file was last checked or updated 20221125

# README for clamtk-gnome

clamtk-gnome is a simple plugin for
[clamtk](https://github.com/dave-theunsub/clamtk) to allow a right-click, context menu scan of files or folders in the Nautilus file manager.


## Installation

This section gives different options for installing clamtk-gnome.

Please note that you may need to add `sudo` before the installation commands for Ubuntu and Debian-based systems.

### Option A: Installation from downloaded package

There are deb and rpm packages to install this plugin:

#### On Debian based systems (Ubuntu etc)

`dpkg -i clamtk-gnome_6.15-1_all.deb`

`apt-get install -f`

#### On CentOS systems

`yum install clamtk-gnome-6.15-1.fc.noarch.rpm`

#### On Fedora systems

`dnf install clamtk-gnome-6.15-1.fc.noarch.rpm`

### Option B: Manual installation

1. Install [clamtk](https://github.com/dave-theunsub/clamtk/releases)
2. Additionally, you need to install these packages:
  * For Debian/Ubuntu based systems: `python-nautilus`
  * For RedHat/Fedora based systems: `nautilus-python`
3. Download the .tar.xz file
4. As root: `cp clamtk-gnome.py /usr/share/nautilus-python/extensions/`
5. Restart Nautilus or log out and log back in


## Usage and screenshots

1. Bring up the context menu either by
   1. right clicking on a directory:
   
   ![starting scan alt 1](_img/starting_scan_alt1.png)
   
   2. Or by clicking here:
   
   ![starting scan alt 2](_img/starting_scan_alt2.png)

2. Click on the scan button

3. Wait for the scan to complete (pleate note that it may take a couple of seconds for the scan to start and also for the "No threats found" message to be shown at the end - even after the message "Scanning completed" has been shown)
![scan result](_img/scan_result.png)


## Dependencies

* `clamtk` >= 6.00
* On Debian based systems: `python-nautilus`
* On Red Hat based systems: `nautilus-python`
* nautilus-python 4 with >= 6.15

## Links

* https://github.com/dave-theunsub/clamtk-gnome
* https://gitlab.com/dave_m/clamtk-gnome
* http://standards.freedesktop.org/desktop-entry-spec/latest/

## Contact

* Dave M, dave.nerd @gmail.com
