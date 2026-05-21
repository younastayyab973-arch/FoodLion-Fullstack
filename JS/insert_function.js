const fs = require('fs');
const path = require('path');

const scriptPath = 'e:\\FoodLion\\JS\\script.js';
const content = fs.readFileSync(scriptPath, 'utf8');
const lines = content.split('\n');

// Find the line after checkUserSession function ends and before "9. CART COUNT BADGE"
let insertIndex = -1;
for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('9. CART COUNT BADGE')) {
        insertIndex = i;
        break;
    }
}

if (insertIndex === -1) {
    console.error('Could not find insertion point');
    process.exit(1);
}

// The new function to insert
const newFunction = `/* =========================================
    8b. ACTIVE LINK MANAGEMENT (Dynamic)
    ========================================= */
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav ul li a:not(.btn)');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });
}
`;

// Insert the new function before line insertIndex
lines.splice(insertIndex, 0, newFunction);

// Write back to file
fs.writeFileSync(scriptPath, lines.join('\n'), 'utf8');
console.log('Function inserted successfully at line ' + insertIndex);
