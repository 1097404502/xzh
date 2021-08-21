```bash


server_ip='192.168.66.3'

cat > /root/admin-openrc <<"EOF"
export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=project1
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=admin_pass
export OS_AUTH_URL=http://${server_ip}:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_VOLUME_API_VERSION=2
EOF



```