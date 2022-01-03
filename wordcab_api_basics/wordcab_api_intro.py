import requests

apikey = "YOUR_API_KEY"

# RETRIEVE ACCOUNT DETAILS

endpoint = "https://wordcab.com/api/me"

params = {
    "apikey": apikey
}

r = requests.get(endpoint, params=params)
r.json()

# UPLOAD AUDIO

file_name = "sales_call.mp3" # <= Change this
file_path = f"/content/{file_name}"
endpoint = "https://wordcab.com/api/upload/" # <= Slash required

files = {
    "audio_file": open(file_path, "rb")
}
params = {
    "apikey": apikey,
    "source": "audio",
    "only_api": "false" # <= set to "true" by default
}

r = requests.post(endpoint, files=files, params=params)
job_name = r.json()["job_name"]

print(job_name)

# POLL JOB STATUS

endpoint = "https://wordcab.com/api/upload/"

params = {
    "apikey": apikey,
    "job_name": job_name, 
}

r = requests.get(endpoint, params=params) # <= When status is "Complete", the dictionary will auto-populate with the summary
r.json()