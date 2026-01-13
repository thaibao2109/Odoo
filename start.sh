#!/bin/bash

# Script to start Odoo server
# Usage: ./start.sh [database_name]

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Starting Odoo Server ===${NC}\n"

# Configuration
ODOO_BIN="/Users/baonguyen/Desktop/app/odoo-source/odoo-bin"
CONFIG_FILE="/Users/baonguyen/Desktop/app/Odoo/odoo.conf"
DB_NAME="${1:-odoo}"
PORT=8069

# Check if Odoo binary exists
if [ ! -f "$ODOO_BIN" ]; then
    echo -e "${RED}✗ ERROR: Odoo binary not found at $ODOO_BIN${NC}"
    exit 1
fi

# Check if config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}✗ ERROR: Config file not found at $CONFIG_FILE${NC}"
    exit 1
fi

# Check if port is already in use
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${YELLOW}⚠ WARNING: Port $PORT is already in use${NC}"
    echo -e "${YELLOW}Use './stop.sh' to stop the existing server first${NC}"
    read -p "Do you want to stop the existing server and start a new one? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./stop.sh
        sleep 2
    else
        exit 1
    fi
fi

echo -e "${BLUE}Starting Odoo with:${NC}"
echo -e "  Binary: $ODOO_BIN"
echo -e "  Config: $CONFIG_FILE"
echo -e "  Database: $DB_NAME"
echo -e "  Port: $PORT"
echo ""
echo -e "${GREEN}Access Odoo at: http://localhost:$PORT${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop${NC}"
echo ""

# Run Odoo
python3 "$ODOO_BIN" -c "$CONFIG_FILE" -d "$DB_NAME" "$@"
