#!/bin/bash

# Script to stop Odoo server

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Stopping Odoo Server ===${NC}\n"

PORT=8069

# Find and kill Odoo processes
PIDS=$(lsof -ti:$PORT 2>/dev/null)

if [ -z "$PIDS" ]; then
    # Try to find by process name
    PIDS=$(ps aux | grep "[o]doo-bin" | grep -v grep | awk '{print $2}')
fi

if [ -n "$PIDS" ]; then
    echo -e "${YELLOW}Found Odoo processes: $PIDS${NC}"
    for PID in $PIDS; do
        echo -e "${YELLOW}Stopping process $PID...${NC}"
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
