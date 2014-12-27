Title: OpenStack Heat Client & Connecting To Rackspace Cloud
Date: 2014-09-19 14:09
Tags: rackspace, openstack, heat, nova

This is primarily to help me remember, and to help anyone who finds this
via Google.

If you're trying to use the rackspace-novaclient tool to connect to
RackSpace's Public Cloud, and you want to use the Heat client as well,
you need to do a little tweaking.

OS\_PASSWORD needs to be the actual password for the account, not the
API key as the novaclient instructions say.

OS\_AUTH\_SYSTEM needs to be unset.

Here's my rcfile, working for both nova and heat clients:  

    :::bash
    export OS_USERNAME=account_name
    export OS_TENANT_NAME=account_number
    export OS_PASSWORD=account_password
    export OS_AUTH_URL=https://identity.api.rackspacecloud.com/v2.0/
    export OS_REGION_NAME=ORD
    export OS_NO_CACHE=1
    export NOVA_RAX_AUTH=1
    export OS_PROJECT_ID=$OS_TENANT_NAME
    export OS_TENANT_ID=$OS_TENANT_NAME
    export HEAT_URL=https://ord.orchestration.api.rackspacecloud.com/v1/${OS_TENANT_ID}

The above tweaks were courtesy of [Evan
Callicoat](https://twitter.com/Thediopter), who is badass.
