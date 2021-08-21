# 57ea696: Add cluster table and related methods … 

57ea6967bf0b553f9c0b22ccf93ce64eafe53a25


Add cluster table and related methods

This patch adds a new table called clusters with its ORM representation
class -Cluster-, and related DB methods.

It also updates DB tables for resources from Cinder Volume nodes that
are addressed by host to include a reference to the cluster
(cluster_name) and related DB methods.

This is part of the effort to support HA A-A in c-vol nodes.

Specs: https://review.openstack.org/327283
Change-Id: I10653d4a5fe4cb3fd1f8ccf1224938451753907e
Implements: blueprint cinder-volume-active-active-support


