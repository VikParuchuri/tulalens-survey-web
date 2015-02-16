Overview
-----------------

Backend code for [Tulalens](www.tulalens.org).

Installation
-----------------

## Easy way -- use Vagrant

* Download vagrant here:  http://www.vagrantup.com/downloads
* Download virtualbox here: https://www.virtualbox.org/wiki/Downloads
* Make a folder called tulalens
* Get into the tulalens folder -- `cd tulalens`
* Clone this repo (`git clone https://github.com/VikParuchuri/TulaLensSurvey.git`) into the tulalens folder.
* `cd tulalens/vagrant`
* Initialize the vagrant machine -- `vagrant up` .  This will take a while, and produce a lot of output.  You'll need to wait a minute or two after the command finishes before you can access the site.


Usage
-------------------

* Make surveys by making a new `.yaml` file in the `surveys` folder.
* Sync surveys with `python sync_surveys.py`.