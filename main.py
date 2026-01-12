from flask import Flask, render_template_string, jsonify
import time

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp DP Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        .animate-spin {
            animation: spin 1s linear infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .animate-pulse {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
    </style>
</head>
<body class="min-h-screen bg-slate-900 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-slate-800 rounded-2xl shadow-2xl p-8">
        <!-- Header -->
        <div class="text-center mb-8">
            <div class="bg-green-600 w-20 h-20 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-12 h-12 text-white" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                </svg>
            </div>
            <h1 class="text-3xl font-bold text-white mb-2">WhatsApp DP Downloader</h1>
        </div>

        <!-- Input Form -->
        <form id="searchForm" onsubmit="searchDP(event)">
            <div class="mb-6">
                <label class="block text-slate-300 mb-2 font-medium">Enter Phone Number</label>
                <input 
                    type="text" 
                    id="phoneInput"
                    name="phone"
                    placeholder="+94 XX XXX XXXX"
                    class="w-full px-4 py-3 bg-slate-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 border border-slate-600"
                    required
                >
            </div>

            <!-- Search Button -->
            <button 
                type="submit"
                id="searchBtn"
                class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-lg transition duration-200 mb-6"
            >
                Search
            </button>
        </form>

        <!-- Loading Area -->
        <div id="loadingArea" class="hidden">
            <div class="bg-slate-700 rounded-lg p-8">
                <div class="text-center">
                    <svg class="animate-spin w-16 h-16 text-green-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    <p id="loadingText" class="text-white text-lg font-medium animate-pulse">Connecting to WhatsApp...</p>
                </div>
            </div>
        </div>

        <!-- Result Area -->
        <div id="resultArea" class="hidden">
            <div class="bg-slate-700 rounded-lg p-6">
                <div id="dpContent"></div>
            </div>
        </div>
    </div>

    <script>
        const loadingMessages = [
            "Connecting to WhatsApp...",
            "Fetching profile data...",
            "Loading profile picture...",
            "Verifying...",
            "Almost done..."
        ];

        async function searchDP(event) {
            event.preventDefault();
            
            const phone = document.getElementById('phoneInput').value.trim();
            const searchBtn = document.getElementById('searchBtn');
            const loadingArea = document.getElementById('loadingArea');
            const resultArea = document.getElementById('resultArea');
            const loadingText = document.getElementById('loadingText');
            
            // Disable button and show loading
            searchBtn.disabled = true;
            searchBtn.classList.add('opacity-50', 'cursor-not-allowed');
            resultArea.classList.add('hidden');
            loadingArea.classList.remove('hidden');

            let messageIndex = 0;
            loadingText.textContent = loadingMessages[0];

            // Change loading message every second
            const messageInterval = setInterval(() => {
                messageIndex++;
                if (messageIndex < loadingMessages.length) {
                    loadingText.textContent = loadingMessages[messageIndex];
                }
            }, 1000);

            try {
                // Send request to Flask backend
                const response = await fetch('/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'phone=' + encodeURIComponent(phone)
                });

                const data = await response.json();

                // Clear interval and hide loading
                clearInterval(messageInterval);
                loadingArea.classList.add('hidden');
                resultArea.classList.remove('hidden');
                searchBtn.disabled = false;
                searchBtn.classList.remove('opacity-50', 'cursor-not-allowed');

                const dpContent = document.getElementById('dpContent');

                if (data.status === 'found') {
                    dpContent.innerHTML = `
                        <div class="text-center">
                            <img src="${data.image}" alt="Profile Picture" class="w-48 h-48 rounded-full mx-auto mb-4 object-cover border-4 border-green-500">
                            <h3 class="text-white text-xl font-semibold mb-2">Profile Picture Found</h3>
                            <p class="text-slate-400 mb-4">Visibility: ${data.visibility}</p>
                            <a href="${data.image}" download class="inline-block bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg transition duration-200">
                                Download
                            </a>
                        </div>
                    `;
                } else if (data.status === 'no_dp') {
                    dpContent.innerHTML = `
                        <div class="text-center py-8">
                            <svg class="w-24 h-24 text-slate-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                            <h3 class="text-white text-xl font-semibold mb-2">NO DP Available</h3>
                            <p class="text-slate-400">This user has not set a profile picture</p>
                        </div>
                    `;
                } else {
                    dpContent.innerHTML = `
                        <div class="text-center py-8">
                            <svg class="w-24 h-24 text-red-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                            </svg>
                            <h3 class="text-white text-xl font-semibold mb-2">Number Not Found</h3>
                            <p class="text-slate-400">Could not find profile for this number</p>
                        </div>
                    `;
                }
            } catch (error) {
                clearInterval(messageInterval);
                loadingArea.classList.add('hidden');
                searchBtn.disabled = false;
                searchBtn.classList.remove('opacity-50', 'cursor-not-allowed');
                alert('An error occurred. Please try again.');
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/search', methods=['POST'])
def search():
    from flask import request
    
    # Add 5 second delay for loading effect
    time.sleep(5)
    
    phone = request.form.get('phone', '').strip()
    
    # Check phone numbers and return appropriate response
    if phone in ['+94 74 338 1623', '+94743381623', '0743381623']:
        return jsonify({
            'status': 'found',
            'image': 'https://raw.githubusercontent.com/dkdesignlk/DP-Downloader/refs/heads/main/functions/asitha.jpg',
            'visibility': 'Everyone'
        })
    elif phone in ['+94 76 347 7532', '+94763477532', '0763477532']:
        return jsonify({
            'status': 'found',
            'image': 'https://raw.githubusercontent.com/dkdesignlk/DP-Downloader/refs/heads/main/functions/ayiya.jpg',
            'visibility': 'My Contacts Only'
        })
    elif phone in ['+94 71 462 9230', '+94714629230', '0714629230']:
        return jsonify({
            'status': 'no_dp'
        })
    else:
        return jsonify({
            'status': 'not_found'
        })

if __name__ == '__main__':
    app.run(host='localhost', port=9093, debug=True)
