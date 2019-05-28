from tciaclient import TCIAClient
import urllib2, urllib,sys
tcia_client = TCIAClient(apiKey = "668e7ae2-f043-4656-ab26-01005f443820",baseUrl="https://services.cancerimagingarchive.net/services/v3",resource = "TCIA")
tcia_client2 = TCIAClient(apiKey ="668e7ae2-f043-4656-ab26-01005f443820",baseUrl="https://services.cancerimagingarchive.net/services/v3",resource="SharedList")
 
#tcia_client.get_image(seriesInstanceUid ="1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440" , downloadPath ="./", zipFileName ="images.zip");
r= tcia_client.get_series(collection = "CPTAC-CM", modality = "pathology" , studyInstanceUid = None , outputFormat = "json" )
#r = tcia_client2.contents_by_name(name="C3N-03617-23")
with open("sam_contents_by_name.json",'w+') as f:
    contents = r.read()
    f.write(contents)
