# -*- coding: utf-8 -*-
'''
Authors: Tim Hessels
         UNESCO-IHE 2016
Contact: t.hessels@unesco-ihe.org
Repository: https://github.com/wateraccounting/watools
Module: Collect/GLEAM
'''
from __future__ import print_function

import sys
from watools.Collect.GLEAM.DataAccess import DownloadData


def main(Dir, Startdate, Enddate, latlim, lonlim, cores=False, Waitbar = 1):
    """
    This function downloads GLEAM monthly data for the specified time
    interval, and spatial extent.

    Keyword arguments:
    Dir -- 'C:/file/to/path/'
    Startdate -- 'yyyy-mm-dd'
    Enddate -- 'yyyy-mm-dd'
    latlim -- [ymin, ymax]
    lonlim -- [xmin, xmax]
	 cores -- amount of cores used
    Waitbar -- 1 (Default) will print a waitbar
    """
    TimeCase = 'monthly'

    print('\nDownload monthly GLEAM Potential ET data for the period %s till %s' %(Startdate, Enddate))

    DownloadData(Dir, Startdate, Enddate, latlim, lonlim, Waitbar, cores, TimeCase, Product = "ETpot")

if __name__ == '__main__':
    main(sys.argv)