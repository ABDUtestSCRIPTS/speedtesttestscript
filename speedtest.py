import speedtest


test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Download Speed : {download}\n
        Upload Speed : {upload}")
        
def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ Internet Speed Test +++   #"
	Space(9); print "#     Script by WH173 5P1D3R    #"
	Space(9); print "#####################################"
	
Credit()
Speedtest()