#!/bin/bash

# Script to restart Odoo server
# Usage: ./restart.sh [database_name]

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Odoo Server Restart ===${NC}\n"

# Configuration
ODOO_BIN="/Users/baonguyen/Desktop/app/odoo-source/odoo-bin"
CONFIG_FILE="/Users/baonguyen/Desktop/app/Odoo/odoo.conf"
DB_NAME="${1:-odoo}"
PORT=8069

# Function to check if Odoo is running
check_odoo_running() {
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        return 0  # Running
    else
        return 1  # Not running
    fi
}

# Function to stop Odoo
stop_odoo() {
    echo -e "${YELLOW}Stopping Odoo server...${NC}"
    
    # Find and kill Odoo processes
    PIDS=$(lsof -ti:$PORT 2>/dev/null)
    
    if [ -z "$PIDS" ]; then
        # Try to find by process name
        PIDS=$(ps aux | grep "[o]doo-bin" | grep -v grep | awk '{print $2}')
    fi
    
    if [ -n "$PIDS" ]; then
        echo -e "${YELLOW}Found Odoo processes: $PIDS${NC}"
        for PID in $PIDS; do
            echo -e "${YELLOW}Killing process $PID...${NC}"
            kill $PID 2>/dev/null
        done
        
        # Wait for processes to stop
        echo -e "${YELLOW}Waiting for processes to stop...${NC}"
        sleep 3
        
        # Force kill if still running
        for PID in $PIDS; do
            if kill -0 $PID 2>/dev/null; then
                echo -e "${RED}Force killing process $PID...${NC}"
                kill -9 $PID 2>/dev/null
            fi
        done
        
        sleep 2
        echo -e "${GREEN}✓ Odoo server stopped${NC}\n"
    else
        echo -e "${GREEN}✓ Odoo server is not running${NC}\n"
    fi
}

# Function to start Odoo
start_odoo() {
    echo -e "${YELLOW}Starting Odoo server...${NC}"
    
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
    
    # Start Odoo in background
    echo -e "${BLUE}Starting Odoo with:${NC}"
    echo -e "  Binary: $ODOO_BIN"
    echo -e "  Config: $CONFIG_FILE"
    echo -e "  Database: $DB_NAME"
    echo -e "  Port: $PORT"
    echo ""
    
    # Run Odoo in background
    nohup python3 "$ODOO_BIN" -c "$CONFIG_FILE" -d "$DB_NAME" > /dev/null 2>&1 &
    
    # Wait a bit for server to start
    sleep 3
    
    # Check if server started successfully
    if check_odoo_running; then
        echo -e "${GREEN}✓ Odoo server started successfully!${NC}"
        echo -e "${GREEN}✓ Access Odoo at: http://localhost:$PORT${NC}\n"
    else
        echo -e "${RED}✗ ERROR: Odoo server failed to start${NC}"
        echo -e "${YELLOW}Check logs at: /Users/baonguyen/Desktop/app/Odoo/odoo.log${NC}"
        exit 1
    fi
}

# Main execution
echo -e "${BLUE}Step 1: Stopping Odoo server...${NC}"
stop_odoo

echo -e "${BLUE}Step 2: Starting Odoo server...${NC}"
start_odoo

echo -e "${GREEN}=== Restart Complete ===${NC}"
echo -e "${YELLOW}To view logs: tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log${NC}"
echo -e "${YELLOW}To stop server: ./stop.sh${NC}"
