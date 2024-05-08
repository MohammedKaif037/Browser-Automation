import webbrowser as wb
def web_auto():

    msedge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    URLS = ["stackoverflow.com",
      "github.com/MohammedKaif037",
      "google.com",
      "youtube.com",
      "perplexity.ai"         
     ]
    for url in URLS:
        print("Opening", url)
        wb.get(msedge_path).open(url)

web_auto()
