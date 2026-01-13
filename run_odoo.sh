#!/bin/bash

# Script to run Odoo with the order_progress_management module

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Odoo Order Progress Management Runner ===${NC}\n"

# Find Odoo installation
ODOO_BIN=""
ODOO_PATH=""

# Common Odoo locations
POSSIBLE_PATHS=(
    "/Users/baonguyen/Desktop/app/odoo-source/odoo-bin"
    "$HOME/odoo/odoo-bin"
    "$HOME/Odoo/odoo-bin"
    "/opt/odoo/odoo-bin"
    "/usr/local/bin/odoo-bin"
    "$(which odoo-bin 2>/dev/null)"
    "$(python3 -c 'import odoo; print(odoo.__file__.replace("/odoo/__init__.py", "/odoo-bin"))' 2>/dev/null)"
)

for path in "${POSSIBLE_PATHS[@]}"; do
    if [ -f "$path" ] && [ -x "$path" ]; then
        ODOO_BIN="$path"
        ODOO_PATH="$(dirname "$(dirname "$path")")"
        echo -e "${GREEN}✓ Found Odoo at: $ODOO_BIN${NC}"
        break
    fi
done

# If not found, try to find in current directory or parent
if [ -z "$ODOO_BIN" ]; then
    if [ -f "./odoo-bin" ]; then
        ODOO_BIN="./odoo-bin"
        ODOO_PATH="."
    elif [ -f "../odoo-bin" ]; then
        ODOO_BIN="../odoo-bin"
        ODOO_PATH=".."
    fi
fi

# If still not found, provide instructions
if [ -z "$ODOO_BIN" ]; then
    echo -e "${RED}✗ Odoo not found!${NC}"
    echo -e "${YELLOW}Please install Odoo first or specify the path:${NC}"
    echo ""
    echo "Option 1: Install Odoo using pip:"
    echo "  pip3 install odoo"
    echo ""
    echo "Option 2: Clone Odoo from GitHub:"
    echo "  git clone https://github.com/odoo/odoo.git ~/odoo"
    echo ""
    echo "Option 3: Run with custom path:"
    echo "  $0 --odoo-path /path/to/odoo"
    echo ""
    exit 1
fi

# Get current directory (where the module is)
MODULE_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ADDONS_PATH="$MODULE_PATH"

# Database name (default or from argument)
DB_NAME="${1:-odoo_db}"

# Configuration
CONFIG_FILE="$MODULE_PATH/odoo.conf"

# Create config file if it doesn't exist
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${YELLOW}Creating Odoo configuration file...${NC}"
    cat > "$CONFIG_FILE" << EOF
[options]
addons_path = $ADDONS_PATH,$ODOO_PATH/addons
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
db_name = $DB_NAME
http_port = 8069
logfile = $MODULE_PATH/odoo.log
log_level = info
EOF
    echo -e "${GREEN}✓ Configuration file created: $CONFIG_FILE${NC}"
fi

echo -e "\n${GREEN}Starting Odoo...${NC}"
echo -e "Module path: $ADDONS_PATH"
echo -e "Database: $DB_NAME"
echo -e "Port: 8069"
echo -e "\n${YELLOW}Access Odoo at: http://localhost:8069${NC}\n"

# Run Odoo
exec "$ODOO_BIN" -c "$CONFIG_FILE" "$@"
