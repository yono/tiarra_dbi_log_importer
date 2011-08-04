# tiarra dbi log importer 

This script import [tiarra(IRC Proxy)](http://www.clovery.jp/tiarra/) logs to DB [(DBI:Log)](http://d.hatena.ne.jp/woremacx/20080404/1207260356).

## Requirement
- Python (I tested version 2.7.1)
- Python Modules
  - MySQL-Python (I tested version 1.2.3)

## Usage

Firstly, you need to finish these settings.
- tiarra
- DBI::Log

Download tar.gz or git clone this repository.

    $ git clone git://github.com/yono/tiarra_dbi_log_importer.git
    $ cd tiarra_dbi_log_importer

Copy config.ini.sample to config.ini.
    
    $ cp config.ini.sample config.ini

Edit config.ini

    $ vim config.ini

You must input username, password, database name for tiarra.

    [db]
    username=user
    password=pass
    db=database
    charset=utf8

After that, you can run a script tiarra_dbi_log_importer.py

    $ python tiarra_dbi_log_importer.py /locate/to/tiarra/log

