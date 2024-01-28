# README for clamtk-gnome

This readme file was last checked or updated 20240128.

clamtk-gnome is a simple plugin for
[clamtk](https://github.com/dave-theunsub/clamtk) to allow a right-click, context menu scan of files or folders in the Nautilus file manager.

## Installation

This section gives different options for installing clamtk-gnome.

Please note that you may need to add `sudo` before the installation commands for Ubuntu and Debian-based systems.  

First, download clamtk-gnome from its [Github](https://github.com/dave-theunsub/clamtk-gnome) or [Gitlab](https://gitlab.com/dave_m/clamtk-gnome) home.  RPM-based systems like Fedora, RedHat, CentOS, Alma, or Rocky (and others) will use an RPM (.rpm).  DEB-based systems like Debian or Ubuntu will use a DEB (.deb).

### Option A: Double-click to install

This is the easiest and recommended way.  Installing this way allows the system package manager to take care of installation details.  

### Option B: Installation from downloaded package

There are deb and rpm packages to install this plugin:  

#### On Debian based systems (Ubuntu etc)

`dpkg -i clamtk-gnome_6.15-1_all.deb`

`apt-get install -f`

#### On CentOS systems

`yum install clamtk-gnome-6.15-1.fc.noarch.rpm`

#### On Fedora systems

`dnf install clamtk-gnome-6.15-1.fc.noarch.rpm`

### Option C: Manual installation

1. Install [clamtk](https://github.com/dave-theunsub/clamtk/releases)

2. This is the dependency needed:

3. Download the .tar.xz file

4. As root: `cp clamtk-gnome.py /usr/share/nautilus-python/extensions/`

5. Restart Nautilus, or log out and log back in

## Usage and screenshots

1. Bring up the context menu either by
   right clicking on a directory:

   ![starting scan alt 1](_img/starting_scan_alt1.png)

   or by clicking here:

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

[Github clamtk-gnome](https://github.com/dave-theunsub/clamtk-gnome)  
[Gitlab clamtk-gnome](https://gitlab.com/dave_m/clamtk-gnome)  
[Desktop entry spec documentation](http://standards.freedesktop.org/desktop-entry-spec/latest/)  

## Contact

* Dave M, dave.nerd @gmail.com  
[0xC81DF0FAC4AFEB22](https://davem.fedorapeople.org/RPM-GPG-KEY-DaveM-20230506)
