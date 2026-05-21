/**
 * API Configuration
 * Handles backend API connection with fallback support
 */

const API_CONFIG = {
    // Detect API base URL dynamically
    getBaseUrl: function() {
        const hostname = window.location.hostname;
        const protocol = window.location.protocol;
        const port = window.location.port;
        
        // Production-ready logic
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return `${protocol}//${hostname}:8000`;
        }
        
        // Same origin (production)
        return `${protocol}//${hostname}${port ? ':' + port : ''}`;
    },
    
    // Make API requests with proper error handling
    request: async function(endpoint, options = {}) {
        const url = `${this.getBaseUrl()}/api${endpoint}`;
        const token = localStorage.getItem('accessToken') || localStorage.getItem('access_token');
        
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };
        
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        
        try {
            const response = await fetch(url, {
                ...options,
                headers
            });
            
            if (!response.ok) {
                if (response.status === 401) {
                    localStorage.removeItem('accessToken');
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('currentUser');
                    localStorage.removeItem('isAdmin');
                    window.location.href = '/login.html';
                    throw new Error('Session expired. Please login again.');
                }
                throw new Error(`API Error: ${response.status} ${response.statusText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API Request Failed:', error);
            throw error;
        }
    },
    
    // Convenience methods
    get: function(endpoint, options = {}) {
        return this.request(endpoint, { ...options, method: 'GET' });
    },
    
    post: function(endpoint, data, options = {}) {
        return this.request(endpoint, {
            ...options,
            method: 'POST',
            body: JSON.stringify(data)
        });
    },
    
    put: function(endpoint, data, options = {}) {
        return this.request(endpoint, {
            ...options,
            method: 'PUT',
            body: JSON.stringify(data)
        });
    },
    
    delete: function(endpoint, options = {}) {
        return this.request(endpoint, { ...options, method: 'DELETE' });
    }
};

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = API_CONFIG;
}
