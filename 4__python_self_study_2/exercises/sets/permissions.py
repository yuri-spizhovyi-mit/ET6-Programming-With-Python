admin_permissions = {"read", "write", "delete"}
user_permissions = {"read", "write"}
missing_permissions = admin_permissions - user_permissions
print(missing_permissions)
