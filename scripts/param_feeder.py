#!/usr/bin/env python
#
# License: MIT
#   https://raw.github.com/stonier/feed_the_troll/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Feed the troll a rosparam namespace!
"""

##############################################################################
# Imports
##############################################################################

import feed_the_troll
import rospy

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':

    rospy.init_node("feed_parameters")
    service_namespace = rospy.get_param("~service_namespace")
    feeder = feed_the_troll.feeders.ROSParameters(service_namespace=service_namespace)
    rospy.spin()
