template: index.html

Table test 
======

| ddd |    |   |    |    |
|-----|----|---|----|----|
|     | dd |   |    | dd |
|     |    |   | dd |    |
|     |    |   |    | dd |
|     | dd |   |    | dd |
|     |    |   | dd |    |
|     |    |   |    | dd |
|     | dd |   |    | dd |
|     |    |   | dd |    |
|     |    |   |    | dd |
|     | dd |   |    | dd |

@todo the table does not look nice

OpenvCloud 4.0 Product Spec
===========================

Intro
-----
OpenvCloud is a hyperconverged private/public cloud platform.

OpenvCloud 4.0 Appliances
-------------------------

- OpenvCloud combined node
  - combined storage & compute node
  - used in a 1 tier deployment
  - is a 2U server with 8 disks inside of 2 or 4 TB
  - each combined node has a certain amount of compute & storage capacity and exists in multiple capacity sizes
  - if redundancy is required then at least 3 nodes are required
  - they are ideally used on remote office use case or for the smaller deployments
- OpenvCloud compute cluster
  - each cluster has 4 nodes
  - a cluster is 2U high and can host upto 400 vmachines
  - a compute cluster exists in 2 flavors (128 or 256 GB memory per node)
- OpenvCloud storage cluster
  - each cluster has 4 storage blades, each storage blade has upto 12 disks 
  - a cluster is 4U high and can host upto 48 disks, raw storage 192 TB
  - a storage cluster exists in 4 capacity ranges (64TB,128TB,192TB)
  - a storage cluster of 64 TB can seamless (without downtime) be upgraded to 192TB
- OpenvCloud storage cluster ethernet drives
  - we also support a storage cluster based on seagate ethernet drives, this product will be available end Q1 and need to be further defined
- OpenvCloud router
  - enterprise capable router/firewall/vpn
  - allows seamless integration between (home) office and cloud
  - exists in multiple form factors depending required performance
- OpenvCloud Thin Client (Q2 2015)
  - ultra small & power efficient thin client allows zero management access to the cloud

OpenvCloud components
---------------------
- OpenvCloud Portal
  - Customers use this portal to provision their capacity on 1 or more of their OpenvCloud Appliances.
  - The portal is very easy to use and allows easy deployment of vmachines and cloud desktops
  - The portal has an easy to use API which allows full management of the cloud capacity.
  - The portal is hosted and operated by GreenITGlobe in a global redundant way.
- OpenvCloud Controller
  - OpenvCloud Controller is the management engine of X nr of OpenvCloud Appliances and takes care of
    - monitoring of full health of the systems
    - capacity planning
    - billing engine
    - remote control of OpenvCloud Appliances even if the appliances are installed begind firewalls on premises of the customer.
    - expansion of grids (add appliances & activate their utilization)    
    - management of the OpenvCloud vSAN, DSS & VFS
    - management of OpenvCloud defense shields and OpenvCloud routers.
  - The controller also has a rebrandable wiki based Portal allowing operators to manage their cloud deployments.
  - The controller gives full visibility on the health of your appliances.
  - The controller also gives the operator the ability to securely access the openstack operator UI.
  - The controller is hosted & operated by GreenITGlobe but private per customer or reseller.
- OpenvCloud OpenStack 
  - OpenvCloud uses OpenStack as underlying cloud platform.
  - All features from OpenStack are available to our customers and also the UI can be used to manage the cloud (but is not required).
  - We have create our own distribution & management system on top of OpenStack.
  - We have integrated another networking layer inside OpenStack (the std networking layer is too complex and errorprone and has scalability issues).
- OpenvCloud vSAN
  - Ultra reliable & scalable storage system for virtual machines.
  - Upto 50k IOPS are available per compute node.
  - OpenvCloud vSAN is 100% integrated in OpenStack (plugin to cinder)
  - The OpenvCloud vSAN supports unlimited snapshots, thin provisioning & full virtual machine storage live cycle management.
- OpenvCloud DSS
  - Ultra scalable object based storage system.
  - OpenvCloud DSS is extremely fast (upto 2 GByte per second per storage front end node) and scales to hundreds of petabytes if required. 
  - Interface to OpenvCloud DSS is an S3 interface.
- OpenvCloud VFS (Virtual Filesystem).
  - is the ideal choice for generic usable 2ndary storage system.
  - OpenvCloud VFS has a command line interface used to import/export files or directories into the VFS
  - OpenvCloud VFS has an FTP & CIFS gateway which allows a unified namespace onto the storage pool.
  - OpenvCloud VFS is not meant to be used for primary storage workloads (random access to files or files in read/write mode). 
  - OpenvCloud VFS allows you to split your storage pool (which is combination of all disks) in namespaces.
  - Each OpenvCloud VFS namespace support dedupe which means that data will be stored uniquely over the pool.
  - OpenvCloud VFS has a rest interface to interact with the namespaces.
  - The system is ultra scalable and reliable. The metadata as well as the data is distributed over the full cloud.
- OpenvCloud Defense Shield (virtual firewalling & routing layer)
  - The OpenvCloud defense shield allows the customers to protect their cloud spaces (secure networking zones in the cloud).
  - The Defense Shield can be used to create tunnels towards the OpenvCloud routers.
- OpenvCloud IT Broker
  - Enable legacy apps to be accessed through any HTML5 capable browser.
- OpenvCloud VDI (Q2 2015)
  - easy to use VDI solution layered on top of OpenvCloud.
  - Access over HTML5 browser.
- OpenvCloud Desktop (Q2 2015)
  - private dropbox alternative with very nice web UI & sync client for desktops.
  - ideal to share your files in a secure way.
  - all data stays securely in your cloud.



