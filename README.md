This readme file was last updated 6 Oct 2016

# README for ClamTkGnome

ClamTkGnome is a simple plugin for [ClamTk](https://github.com/dave-theunsub/clamtk) to allow a right-click, context menu scan of files or folders in the Nautilus file manager


## Installation

### Automatic installation

There are deb and rpm packages to install this plugin:

#### On Debian based systems (Ubuntu etc)

`sudo apt-get install clamtk-gnome`

#### On Red Hat based systems

`rpm -i clamtk-gnome`

### Manual installation

1. Install [ClamTk](https://github.com/dave-theunsub/clamtk). You'll need version 4.00 or newer.
2. Additionally, you need to install these packages:
  * For Debian based systems: `python-nautilus`
  * For Red Hat based systems: `nautilus-python`
3. Download the project files
4. As root run `cp clamtk-gnome.py /usr/share/nautilus-python/extensions/`
5. Restart Nautilus


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

* `clamtk` >= 4.00
* On Debian based systems: `python-nautilus`
* On Red Hat based systems: `nautilus-python`

## Links

* http://dave-theunsub.github.io/clamtk/
* https://github.com/dave-theunsub/clamtk-gnome
* https://gitlab.com/dave_m/clamtk-gnome
* https://bitbucket.org/dave_theunsub/clamtk-gnome
* http://standards.freedesktop.org/desktop-entry-spec/latest/
* http://code.google.com/p/clamtk/ (no longer used)

## Contact

* Dave M, dave.nerd AT gmail DOT com
* Tord D, tord.dellsen AT gmail DOT com
