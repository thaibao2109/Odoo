/** @odoo-module **/

import { Component, onMounted, onWillUpdateProps, useRef, useEffect } from "@odoo/owl";
import { registry } from "@web/core/registry";

// Function to highlight status buttons based on current status
function highlightStatusButtons() {
    const statusBars = document.querySelectorAll('.progress_status_bar');
    statusBars.forEach(bar => {
        // Try to find the status field
        let statusField = bar.querySelector('input[name="progress_status"]');
        if (!statusField) {
            // Try to find in parent form
            const form = bar.closest('.o_form_view');
            if (form) {
                statusField = form.querySelector('input[name="progress_status"]');
            }
        }
        
        if (!statusField) return;
        
        const currentStatus = statusField.value;
        const buttons = bar.querySelectorAll('.status_step');
        
        buttons.forEach(btn => {
            btn.classList.remove('status_active', 'status_cancelled');
            if (btn.dataset.status === currentStatus) {
                btn.classList.add('status_active');
                if (currentStatus === 'cancelled') {
                    btn.classList.add('status_cancelled');
                }
            }
        });
    });
}

// Run on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', highlightStatusButtons);
} else {
    highlightStatusButtons();
}

// Re-highlight after form updates (for Odoo's dynamic form loading)
setInterval(highlightStatusButtons, 1000);

// Also highlight when buttons are clicked
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('status_step')) {
        setTimeout(highlightStatusButtons, 100);
    }
});
