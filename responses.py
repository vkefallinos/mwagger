list_clouds = [
    {"state": "online", "apikey": "XYZ_replaced", "tenant_name": "", "title": "Linode",
     "enabled": True, "region": "", "provider": "linode", "poll_interval": 10000, "id": "HiYUF5YDyxdfaNpxSs6FQakw4Wb"},
    {"state": "online", "apikey": "XYZ_replaced", "tenant_name": "", "title": "DigitalOcean",
        "enabled": True, "region": "", "provider": "digitalocean", "poll_interval": 10000, "id": "2UmAeuwfMZRMHz9bTFEE9zmEm1hJ"},
    {"state": "online", "apikey": "unwebme", "tenant_name": "", "title": "Rackspace Chicago", "enabled": True, "region": "ord", "provider": "rackspace", "poll_interval": 10000,
        "id": "2zMXgapqqaw9bSNUzSmuygFLy6Kp"}
]

check_auth = {"api_token": "4a2c2j08099809709as098087832843e561abb495c4a30726a8590f73adad", "current_plan": {"machine_limit": 20, "promo_code": "", "title": "Startup", "started": 1438165757.799234,
                                                                                                                "isTrial": True, "has_expired": True, "expiration": 1439461757.799246}, "user_details": {"country": "", "number_of_servers": "", "number_of_people": "", "name": " ", "company_name": ""}}
add_cloud = {"state": "online", "apikey": "XYZ_replaced", "tenant_name": "", "title": "Linode",
     "enabled": True, "region": "", "provider": "linode", "poll_interval": 10000, "id": "HiYUF5YDyxdfaNpxSs6FQakw4Wb"}
    
list_sizes = [
 {
  "name": "512mb", 
  "price": "$0.00744/hour, $5.0/month",
  "ram": "512mb", 
  "driver": "Digital Ocean",
  "bandwidth": 0,
  "disk": "20G SSD",
  "id": "512mb"},
 {
  "name": "1gb",
  "price": "$0.01488/hour",
  "ram": "1gb", 
  "driver": "Digital Ocean",
  "bandwidth": 0,
  "disk": "30G SSD",
  "id": "1gb"
 }
]

list_machines=[
 {"can_start": False, "tags": [], "can_destroy": True, "private_ips": [], "imageId": None, "can_tag": False, "id": "4499827", "size": None, "can_reboot": True, "uuid": "4cb9ffc3787dd801b022be449427920d71ebec34", "can_stop": True, "extra": {"kernel": {"version": "3.2.0-4-amd64", "id": 3285, "name": "Debian 7.0 x64 vmlinuz-3.2.0-4-amd64 (3.2.65-1+deb7u1)"}, "name": "monitor.markos.com", "backup_ids": [], "created_at": "2015-03-17T14:49:09Z", "features": ["virtio"], "memory": 512, "disk": 20, "image": {"min_disk_size": 20, "slug": "debian-7-0-x64", "name": "7.0 x64", "created_at": "2015-01-28T16:09:29Z", "id": 10322059, "regions": ["nyc1", "ams1", "sfo1", "nyc2", "ams2", "sgp1", "lon1", "nyc3", "ams3", "fra1", "tor1"], "distribution": "Debian", "type": "snapshot", "public": True}, "size": {"price_monthly": 5.0, "available": True, "transfer": 1.0, "price_hourly": 0.00744, "regions": ["nyc1", "sgp1", "ams1", "sfo1", "nyc2", "lon1", "nyc3", "ams3", "ams2", "fra1"], "vcpus": 1, "memory": 512, "disk": 20, "slug": "512mb"}}, "public_ips": ["107.170.218.51"], "name": "monitor.markos.com", "state": "running", "can_rename": True}, 

{"can_start": False, "tags": [], "can_destroy": True, "private_ips": ["10.128.253.139"], "imageId": None, "can_tag": False, "id": "6220698", "size": None, "can_reboot": True, "uuid": "a0200f99aa61e2f9a60c96813cf86132778d2cd3", "can_stop": True, "extra": {"kernel": {"version": "3.13.0-57-generic", "id": 5175, "name": "Ubuntu 14.04 x64 vmlinuz-3.13.0-57-generic"}, "name": "kvm", "backup_ids": [], "created_at": "2015-07-20T10:00:00Z", "features": ["private_networking", "virtio"], "memory": 512, "disk": 20, "image": {"min_disk_size": 20, "slug": None, "name": "14.04 x64", "created_at": "2015-07-17T16:39:08Z", "id": 12790328, "regions": ["nyc1", "ams1", "sfo1", "nyc2", "ams2", "sgp1", "lon1", "nyc3", "ams3", "fra1", "tor1"], "distribution": "Ubuntu", "type": "snapshot", "public": False}, "size": {"price_monthly": 5.0, "available": True, "transfer": 1.0, "price_hourly": 0.00744, "regions": ["nyc1", "sgp1", "ams1", "sfo1", "nyc2", "lon1", "nyc3", "ams3", "ams2", "fra1"], "vcpus": 1, "memory": 512, "disk": 20, "slug": "512mb"}}, "public_ips": ["104.131.217.171"], "name": "kvm", "state": "running", "can_rename": True}
]

rename_cloud={"ok":True}

delete_cloud={"ok":True}
list_supported_providers = {"supported_providers": [{"provider": "bare_metal", "title": "Bare Metal Server"}, {"provider": "coreos", "title": "CoreOS"}, {"provider": "azure", "title": "Azure"}, {"provider": "ec2_ap_northeast", "title": "EC2 AP NORTHEAST"}, {"provider": "ec2_ap_southeast", "title": "EC2 AP SOUTHEAST"}, {"provider": "ec2_ap_southeast_2", "title": "EC2 AP Sydney"}, {"provider": "ec2_eu_central", "title": "EC2 EU Frankfurt"}, {"provider": "ec2_eu_west", "title": "EC2 EU Ireland"}, {"provider": "ec2_sa_east", "title": "EC2 SA EAST"}, {"provider": "ec2_us_east", "title": "EC2 US EAST"}, {"provider": "ec2_us_west", "title": "EC2 US WEST"}, {"provider": "ec2_us_west_oregon", "title": "EC2 US WEST OREGON"}, {"provider": "gce", "title": "Google Compute Engine"}, {"provider": "nephoscale", "title": "NephoScale"}, {"provider": "digitalocean", "title": "DigitalOcean"}, {"provider": "linode", "title": "Linode"}, {"provider": "openstack", "title": "OpenStack"}, {"provider": "rackspace:dfw", "title": "Rackspace DFW"}, {"provider": "rackspace:ord", "title": "Rackspace ORD"}, {"provider": "rackspace:iad", "title": "Rackspace IAD"}, {"provider": "rackspace:lon", "title": "Rackspace LON"}, {"provider": "rackspace:syd", "title": "Rackspace AU"}, {"provider": "rackspace:hkg", "title": "Rackspace HKG"}, {"provider": "rackspace_first_gen:us", "title": "Rackspace US (OLD)"}, {"provider": "rackspace_first_gen:uk", "title": "Rackspace UK (OLD)"}, {"provider": "softlayer", "title": "SoftLayer"}, {"provider": "hpcloud:region-a.geo-1", "title": "HP Helion Cloud - US West"}, {"provider": "hpcloud:region-b.geo-1", "title": "HP Helion Cloud - US East"}, {"provider": "docker", "title": "Docker"}, {"provider": "vcloud", "title": "VMware vCloud"}]}

list_images = [{"star":True,"id":"mist/debian-wheezy","name":"Debian Wheezy","extra":{}},{"star":True,"id":"mist/ubuntu-14.04","name":"Ubuntu 14.04","extra":{}},{"star":True,"id":"mist/fedora-20","name":"Fedora 20","extra":{}},{"star":True,"id":"mist/opensuse-13.1","name":"OpenSUSE 13.1","extra":{}},{"star":False,"id":"593897323df10f7d1c4cd8e132564d9317cdba39216d6ab54c43da326542992c","name":"mist/ubuntu-14.04:latest","extra":{"size":0,"virtual_size":303918585,"created":1425469068}},{"star":False,"id":"626d479eea5ef2b9bc67daaa0f0a3ce6e243d077b8dc6b5c61e8a297c196ec4a","name":"mist/opensuse-13.1:latest","extra":{"size":0,"virtual_size":671177561,"created":1402933596}}]

list_keys = [{"id":"hpcloudisdead","machines":[["3WwgPBXETjdeMEbM5fUCACSvedGT","c5c9b3ee-6beb-478a-8aa7-d132e07880dd",0,None,False,22],["3WwgPBXETjdeMEbM5fUCACSvedGT","83848ff8-6862-429a-b4c2-593628ae1e80",0,None,False,22]],"isDefault":False},{"id":"vasTestKey","machines":[],"isDefault":False},{"id":"markos","machines":[["3ZWJJEemA4hoMaxUZiWQgi686Rvi","i-da06aa76",1448906714.820053,"ubuntu",None,22]],"isDefault":True}]