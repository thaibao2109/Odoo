#!/bin/bash

# Script to create Odoo database manually

DB_NAME="${1:-odoo_db}"
ADMIN_EMAIL="${2:-admin@example.com}"
ADMIN_PASSWORD="${3:-admin}"
LANG="${4:-vi_VN}"

echo "=== Creating Odoo Database ==="
echo "Database name: $DB_NAME"
echo "Admin email: $ADMIN_EMAIL"
echo "Admin password: $ADMIN_PASSWORD"
echo ""

# Create database
/opt/homebrew/opt/postgresql@14/bin/psql -U odoo -d postgres -c "CREATE DATABASE $DB_NAME ENCODING 'utf8' TEMPLATE template0;" 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Database created successfully!"
    echo ""
    echo "Now initialize the database with Odoo:"
    echo "python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c /Users/baonguyen/Desktop/app/Odoo/odoo.conf -d $DB_NAME --stop-after-init --without-demo=all"
    echo ""
    echo "Or with demo data:"
    echo "python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c /Users/baonguyen/Desktop/app/Odoo/odoo.conf -d $DB_NAME --stop-after-init"
    echo ""
    echo "After initialization, you can access: http://localhost:8069"
    echo "Login with: $ADMIN_EMAIL / $ADMIN_PASSWORD"
else
    echo "❌ Failed to create database"
    exit 1
fi
