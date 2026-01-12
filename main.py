from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp DP Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
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
        <div class="mb-6">
            <label class="block text-slate-300 mb-2 font-medium">Enter Phone Number</label>
            <input 
                type="text" 
                id="phoneInput"
                placeholder="+94 XX XXX XXXX"
                class="w-full px-4 py-3 bg-slate-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 border border-slate-600"
            >
        </div>

        <!-- Search Button -->
        <button 
            onclick="searchDP()"
            class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-lg transition duration-200 mb-6"
        >
            Search
        </button>

        <!-- Result Area -->
        <div id="resultArea" class="hidden">
            <div class="bg-slate-700 rounded-lg p-6">
                <div id="dpContent"></div>
            </div>
        </div>
    </div>

    <script>
        function searchDP() {
            const phone = document.getElementById('phoneInput').value.trim();
            const resultArea = document.getElementById('resultArea');
            const dpContent = document.getElementById('dpContent');
            
            if (!phone) {
                alert('Please enter a phone number');
                return;
            }

            resultArea.classList.remove('hidden');

            // Check phone numbers
            if (phone === '+94 74 338 1623' || phone === '+94743381623' || phone === '0743381623') {
                dpContent.innerHTML = `
                    <div class="text-center">
                        <img src="https://raw.githubusercontent.com/dkdesignlk/DP-Downloader/refs/heads/main/functions/asitha.jpg" alt="Profile Picture" class="w-48 h-48 rounded-full mx-auto mb-4 object-cover border-4 border-green-500">
                        <h3 class="text-white text-xl font-semibold mb-2">Profile Picture Found</h3>
                        <p class="text-slate-400 mb-4">Visibility: Everyone</p>
                        <button class="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg transition duration-200">
                            Download
                        </button>
                    </div>
                `;
            } else if (phone === '+94 76 347 7532' || phone === '+94763477532' || phone === '0763477532') {
                dpContent.innerHTML = `
                    <div class="text-center">
                        <img src="https://raw.githubusercontent.com/dkdesignlk/DP-Downloader/refs/heads/main/functions/ayiya.jpg" alt="Profile Picture" class="w-48 h-48 rounded-full mx-auto mb-4 object-cover border-4 border-green-500">
                        <h3 class="text-white text-xl font-semibold mb-2">Profile Picture Found</h3>
                        <p class="text-slate-400 mb-4">Visibility: My Contacts Only</p>
                        <button class="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg transition duration-200">
                            Download
                        </button>
                    </div>
                `;
            } else if (phone === '+94 71 462 9230' || phone === '+94714629230' || phone === '0714629230') {
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
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':

    app.run(host='localhost', port=9093, debug=True)
