#!/usr/bin/env python3
#############################################################################
# twitter_life.py
#----------------------------------------------------------------------------
# Running genetic algorithms and posting the results on twitter.
#############################################################################

import docker

import os, logging, sys

#----------------------------------------------------------------------------

SMART_ROCKETS_PATH = os.path.join ( ".", "smart_rockets" )
SMART_ROCKETS_TAG = "smart_rockets" 

#----------------------------------------------------------------------------

def main ():

    logging.info ( "Building Smart Rockets." )

    docker_client = docker.from_env ()

    smart_rocket_build_tuple = \
            docker_client.images.build ( path = SMART_ROCKETS_PATH,
                                         tag  = SMART_ROCKETS_TAG ) 

    smart_rocket_img = smart_rocket_build_tuple [ 0 ]

    logging.info ( "Running Smart Rockets." )

    output = docker_client.containers.run ( smart_rocket_img.id )

    logging.info ( "Output: "+str(output) )


if __name__ == '__main__':

    logging.basicConfig ( level=logging.INFO )

    sys.exit ( main () )
